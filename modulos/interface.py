
import customtkinter as ctk
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from datetime import datetime
from modulos.persistencia import carregar_dados, salvar_dados

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

SENHA_RESPONSAVEL = "1234"
COR_PRINCIPAL = "#17365D"
COR_FUNDO = "#F2F5F9"

perfil_atual = None
pendencias = []


def iniciar():
    global janela, area_conteudo, titulo_tela
    global resumo_label, perfil_label, btn_resolver

    pendencias.extend(carregar_dados())

    janela = ctk.CTk()
    janela.title("SCPP - Sistema de Controle de Pendências")
    janela.geometry("1100x680")
    janela.minsize(850, 550)

    menu = ctk.CTkFrame(
        janela, width=220, corner_radius=0,
        fg_color=COR_PRINCIPAL
    )
    menu.pack(side="left", fill="y")
    menu.pack_propagate(False)

    ctk.CTkLabel(
        menu, text="SCPP",
        font=("Arial", 30, "bold"),
        text_color="white"
    ).pack(pady=(30, 5))

    ctk.CTkLabel(
        menu, text="Controle de Pendências",
        text_color="white"
    ).pack(pady=(0, 25))

    ctk.CTkButton(
        menu, text="Início",
        command=mostrar_inicio
    ).pack(fill="x", padx=12, pady=5)

    ctk.CTkButton(
        menu, text="Cadastrar pendência",
        command=abrir_cadastro
    ).pack(fill="x", padx=12, pady=5)

    ctk.CTkButton(
        menu, text="Consultar pendências",
        command=abrir_consulta
    ).pack(fill="x", padx=12, pady=5)

    btn_resolver = ctk.CTkButton(
        menu, text="Resolver pendência",
        command=abrir_resolver
    )
    btn_resolver.pack(fill="x", padx=12, pady=5)

    ctk.CTkButton(
        menu, text="Exportar PDF",
        command=exportar_pdf
    ).pack(fill="x", padx=12, pady=5)

    ctk.CTkButton(
        menu, text="Exportar Excel",
        command=exportar_excel
    ).pack(fill="x", padx=12, pady=5)

    ctk.CTkLabel(
        menu, text="Tema",
        text_color="white"
    ).pack(pady=(20, 5))

    ctk.CTkOptionMenu(
        menu, values=["Claro", "Escuro"],
        command=mudar_tema
    ).pack(fill="x", padx=12, pady=5)

    ctk.CTkButton(
        menu, text="SAIR / TROCAR USUÁRIO",
        fg_color="#B83232",
        command=sair_trocar_usuario
    ).pack(side="bottom", fill="x", padx=12, pady=18)

    principal = ctk.CTkFrame(janela, fg_color="transparent")
    principal.pack(
        side="left", fill="both", expand=True,
        padx=20, pady=20
    )

    cabecalho = ctk.CTkFrame(principal)
    cabecalho.pack(fill="x", pady=(0, 15))

    titulo_tela = ctk.CTkLabel(
        cabecalho, text="Painel do SCPP",
        font=("Arial", 22, "bold")
    )
    titulo_tela.pack(side="left", padx=15, pady=15)

    perfil_label = ctk.CTkLabel(
        cabecalho, text="Perfil: não selecionado"
    )
    perfil_label.pack(side="right", padx=15)

    area_conteudo = ctk.CTkFrame(principal)
    area_conteudo.pack(fill="both", expand=True)

    resumo_label = ctk.CTkLabel(
        principal, text="Total: 0 | Pendentes: 0 | Resolvidas: 0",
        font=("Arial", 14, "bold")
    )
    resumo_label.pack(pady=15)

    atualizar_resumo()
    mostrar_inicio()
    janela.after(200, abrir_login)
    janela.mainloop()


def mudar_tema(escolha):
    ctk.set_appearance_mode(
        "light" if escolha == "Claro" else "dark"
    )


def salvar():
    if not salvar_dados(pendencias):
        messagebox.showerror(
            "Erro", "Não foi possível salvar os dados."
        )


def atualizar_resumo():
    total = len(pendencias)
    pendentes = sum(
        p.get("status") == "Pendente" for p in pendencias
    )
    resolvidas = sum(
        p.get("status") == "Resolvida" for p in pendencias
    )

    resumo_label.configure(
        text=f"Total: {total} | Pendentes: {pendentes} | "
             f"Resolvidas: {resolvidas}"
    )


def limpar_conteudo():
    for widget in area_conteudo.winfo_children():
        widget.destroy()


def mostrar_inicio():
    limpar_conteudo()
    titulo_tela.configure(text="Painel do SCPP")

    ctk.CTkLabel(
        area_conteudo,
        text="Sistema de Controle de Pendências de Produção",
        font=("Arial", 21, "bold"),
        wraplength=650
    ).pack(pady=(70, 15))

    ctk.CTkLabel(
        area_conteudo,
        text="Organize registros e acompanhe as pendências "
             "da produção.",
        font=("Arial", 14),
        wraplength=600
    ).pack(pady=10)


def gerar_id():
    numeros = []

    for p in pendencias:
        identificador = p.get("id", "")
        if identificador.startswith("PEN-"):
            try:
                numeros.append(int(identificador[4:]))
            except ValueError:
                pass

    return f"PEN-{max(numeros, default=0) + 1:03d}"


def abrir_cadastro():
    limpar_conteudo()
    titulo_tela.configure(text="Cadastrar pendência")
    campos = {}

    for rotulo, chave in [
        ("Produto:", "produto"),
        ("Operador responsável:", "operador"),
        ("Natureza da pendência:", "natureza")
    ]:
        ctk.CTkLabel(
            area_conteudo, text=rotulo
        ).pack(anchor="w", padx=20, pady=(10, 2))

        campo = ctk.CTkEntry(
            area_conteudo, width=400
        )
        campo.pack(anchor="w", padx=20, pady=3)
        campos[chave] = campo

    def registrar():
        valores = {
            chave: campo.get().strip()
            for chave, campo in campos.items()
        }

        if not all(valores.values()):
            messagebox.showwarning(
                "Atenção", "Preencha todos os campos."
            )
            return

        agora = datetime.now()

        pendencias.append({
            "id": gerar_id(),
            **valores,
            "data": agora.strftime("%d/%m/%Y"),
            "hora": agora.strftime("%H:%M"),
            "status": "Pendente"
        })

        salvar()
        atualizar_resumo()
        messagebox.showinfo(
            "Sucesso", "Pendência cadastrada!"
        )
        abrir_cadastro()

    ctk.CTkButton(
        area_conteudo, text="Salvar pendência",
        command=registrar, width=200
    ).pack(anchor="w", padx=20, pady=20)

def abrir_consulta():
    limpar_conteudo()
    titulo_tela.configure(text="Consultar pendências")

    busca = ctk.CTkEntry(
        area_conteudo,
        placeholder_text="Buscar por ID, produto, operador ou status",
        width=420
    )
    busca.pack(anchor="w", padx=15, pady=12)

    tabela_frame = ctk.CTkFrame(area_conteudo)
    tabela_frame.pack(fill="both", expand=True, padx=10, pady=5)

    colunas = (
        "id", "produto", "operador",
        "natureza", "data", "hora", "status"
    )

    tabela = ttk.Treeview(
        tabela_frame, columns=colunas,
        show="headings", height=14
    )

    titulos = {
        "id": "ID", "produto": "Produto",
        "operador": "Operador", "natureza": "Natureza",
        "data": "Data", "hora": "Hora", "status": "Status"
    }

    for coluna in colunas:
        tabela.heading(coluna, text=titulos[coluna])
        tabela.column(coluna, width=105, minwidth=70)

    barra = ttk.Scrollbar(
        tabela_frame, orient="vertical",
        command=tabela.yview
    )
    tabela.configure(yscrollcommand=barra.set)
    tabela.pack(side="left", fill="both", expand=True)
    barra.pack(side="right", fill="y")

    def pesquisar():
        tabela.delete(*tabela.get_children())
        termo = busca.get().strip().lower()

        for p in pendencias:
            texto = " ".join(
                str(p.get(campo, ""))
                for campo in colunas
            ).lower()

            if termo in texto:
                tabela.insert(
                    "", "end",
                    values=tuple(p.get(campo, "") for campo in colunas)
                )

    ctk.CTkButton(
        area_conteudo, text="Buscar",
        command=pesquisar
    ).pack(anchor="w", padx=15, pady=8)

    busca.bind("<Return>", lambda evento: pesquisar())
    pesquisar()


def abrir_resolver():
    if perfil_atual != "Responsável":
        messagebox.showwarning(
            "Acesso negado",
            "Somente o responsável pode resolver pendências."
        )
        return

    limpar_conteudo()
    titulo_tela.configure(text="Resolver pendência")

    ctk.CTkLabel(
        area_conteudo,
        text="Selecione uma pendência pendente para resolver:"
    ).pack(anchor="w", padx=15, pady=10)

    tabela = ttk.Treeview(
        area_conteudo,
        columns=("id", "produto", "operador", "status"),
        show="headings",
        height=12
    )

    for coluna, titulo in [
        ("id", "ID"),
        ("produto", "Produto"),
        ("operador", "Operador"),
        ("status", "Status")
    ]:
        tabela.heading(coluna, text=titulo)
        tabela.column(coluna, width=140)

    tabela.pack(fill="both", expand=True, padx=10, pady=10)

    for p in pendencias:
        if p.get("status") == "Pendente":
            tabela.insert(
                "", "end",
                values=(
                    p.get("id", ""),
                    p.get("produto", ""),
                    p.get("operador", ""),
                    p.get("status", "")
                )
            )

    def resolver_selecionada():
        if perfil_atual != "Responsável":
            messagebox.showerror(
                "Acesso negado",
                "Somente o responsável pode resolver pendências."
            )
            return

        selecao = tabela.selection()

        if not selecao:
            messagebox.showwarning(
                "Atenção", "Selecione uma pendência."
            )
            return

        identificador = tabela.item(
            selecao[0], "values"
        )[0]

        for p in pendencias:
            if (
                p.get("id") == identificador
                and p.get("status") == "Pendente"
            ):
                p["status"] = "Resolvida"
                p["data_resolucao"] = datetime.now().strftime(
                    "%d/%m/%Y %H:%M"
                )
                salvar()
                atualizar_resumo()
                messagebox.showinfo(
                    "Sucesso", "Pendência resolvida!"
                )
                abrir_resolver()
                return

        messagebox.showwarning(
            "Atenção", "A pendência não está mais pendente."
        )

    ctk.CTkButton(
        area_conteudo, text="Marcar como resolvida",
        command=resolver_selecionada
    ).pack(anchor="w", padx=15, pady=10)


def exportar_pdf():
    try:
        from reportlab.lib.pagesizes import A4, landscape
        from reportlab.pdfgen import canvas
    except ImportError:
        messagebox.showerror(
            "Biblioteca ausente",
            "Instale a biblioteca reportlab para exportar PDF."
        )
        return

    caminho = filedialog.asksaveasfilename(
        defaultextension=".pdf",
        filetypes=[("Arquivo PDF", "*.pdf")],
        title="Salvar relatório PDF"
    )

    if not caminho:
        return

    try:
        pagina = canvas.Canvas(
            caminho, pagesize=landscape(A4)
        )
        largura, altura = landscape(A4)

        pagina.setFont("Helvetica-Bold", 16)
        pagina.drawString(
            40, altura - 40,
            "SCPP - Relatorio de Pendencias"
        )

        pagina.setFont("Helvetica", 9)
        pagina.drawString(
            40, altura - 60,
            f"Gerado em: {datetime.now().strftime('%d/%m/%Y %H:%M')}"
        )

        cabecalhos = [
            ("ID", 40), ("Produto", 100),
            ("Operador", 220), ("Natureza", 330),
            ("Data", 490), ("Hora", 555),
            ("Status", 610)
        ]

        y = altura - 95

        for texto, x in cabecalhos:
            pagina.drawString(x, y, texto)

        y -= 18

        for p in pendencias:
            if y < 45:
                pagina.showPage()
                pagina.setFont("Helvetica", 9)
                y = altura - 45

            valores = [
                ("id", 40), ("produto", 100),
                ("operador", 220), ("natureza", 330),
                ("data", 490), ("hora", 555),
                ("status", 610)
            ]

            for campo, x in valores:
                texto = str(p.get(campo, ""))
                pagina.drawString(x, y, texto[:25])

            y -= 17

        pagina.save()
        messagebox.showinfo(
            "Sucesso", "Relatório PDF exportado!"
        )

    except Exception as erro:
        messagebox.showerror(
            "Erro", f"Não foi possível gerar o PDF:\n{erro}"
        )


def exportar_excel():
    try:
        from openpyxl import Workbook
        from openpyxl.styles import Font, PatternFill, Alignment
    except ImportError:
        messagebox.showerror(
            "Biblioteca ausente",
            "Instale a biblioteca openpyxl para exportar Excel."
        )
        return

    caminho = filedialog.asksaveasfilename(
        defaultextension=".xlsx",
        filetypes=[("Planilha Excel", "*.xlsx")],
        title="Salvar relatório Excel"
    )

    if not caminho:
        return

    try:
        livro = Workbook()
        planilha = livro.active
        planilha.title = "Pendências"

        cabecalhos = [
            "ID", "Produto", "Operador", "Natureza",
            "Data", "Hora", "Status"
        ]
        planilha.append(cabecalhos)

        for celula in planilha[1]:
            celula.font = Font(bold=True, color="FFFFFF")
            celula.fill = PatternFill(
                "solid", fgColor="17365D"
            )
            celula.alignment = Alignment(horizontal="center")

        campos = [
            "id", "produto", "operador", "natureza",
            "data", "hora", "status"
        ]

        for p in pendencias:
            planilha.append([
                p.get(campo, "") for campo in campos
            ])

        for coluna in planilha.columns:
            letra = coluna[0].column_letter
            maior = max(
                len(str(c.value or "")) for c in coluna
            )
            planilha.column_dimensions[letra].width = min(
                maior + 3, 35
            )

        livro.save(caminho)
        messagebox.showinfo(
            "Sucesso", "Planilha Excel exportada!"
        )

    except Exception as erro:
        messagebox.showerror(
            "Erro", f"Não foi possível gerar o Excel:\n{erro}"
        )


def aplicar_permissoes():
    if perfil_atual == "Responsável":
        btn_resolver.configure(state="normal")
    else:
        btn_resolver.configure(state="disabled")


def entrar_funcionario(janela_login):
    global perfil_atual

    perfil_atual = "Funcionário"
    perfil_label.configure(text="Perfil: Funcionário")
    aplicar_permissoes()
    janela_login.destroy()
    mostrar_inicio()


def abrir_tela_senha(janela_login):
    janela_login.withdraw()

    senha_janela = ctk.CTkToplevel(janela)
    senha_janela.title("Acesso do responsável")
    senha_janela.geometry("350x230")
    senha_janela.transient(janela)
    senha_janela.grab_set()

    ctk.CTkLabel(
        senha_janela, text="Acesso do responsável",
        font=("Arial", 18, "bold")
    ).pack(pady=(20, 10))

    campo_senha = ctk.CTkEntry(
        senha_janela, show="*", placeholder_text="Digite a senha"
    )
    campo_senha.pack(padx=20, fill="x", pady=10)
    campo_senha.focus_set()

    def voltar():
        senha_janela.destroy()
        janela_login.deiconify()

    def confirmar():
        global perfil_atual

        if campo_senha.get() == SENHA_RESPONSAVEL:
            perfil_atual = "Responsável"
            perfil_label.configure(text="Perfil: Responsável")
            aplicar_permissoes()
            senha_janela.destroy()
            janela_login.destroy()
            mostrar_inicio()
        else:
            messagebox.showerror(
                "Senha incorreta", "Verifique a senha e tente novamente."
            )
            campo_senha.delete(0, "end")

    ctk.CTkButton(
        senha_janela, text="Entrar",
        command=confirmar
    ).pack(pady=5)

    ctk.CTkButton(
        senha_janela, text="Voltar",
        command=voltar
    ).pack(pady=5)

    campo_senha.bind("<Return>", lambda evento: confirmar())


def abrir_login():
    janela_login = ctk.CTkToplevel(janela)
    janela_login.title("Acesso ao SCPP")
    janela_login.geometry("380x300")
    janela_login.transient(janela)
    janela_login.grab_set()
    janela_login.protocol(
        "WM_DELETE_WINDOW", janela.destroy
    )

    ctk.CTkLabel(
        janela_login, text="SCPP",
        font=("Arial", 30, "bold")
    ).pack(pady=(25, 5))

    ctk.CTkLabel(
        janela_login, text="Selecione seu perfil"
    ).pack(pady=10)

    ctk.CTkButton(
        janela_login, text="FUNCIONÁRIO",
        command=lambda: entrar_funcionario(janela_login)
    ).pack(fill="x", padx=35, pady=8)

    ctk.CTkButton(
        janela_login, text="RESPONSÁVEL",
        command=lambda: abrir_tela_senha(janela_login)
    ).pack(fill="x", padx=35, pady=8)


def sair_trocar_usuario():
    global perfil_atual

    perfil_atual = None
    perfil_label.configure(text="Perfil: não selecionado")
    aplicar_permissoes()
    abrir_login()


if __name__ == "__main__":
    iniciar()
