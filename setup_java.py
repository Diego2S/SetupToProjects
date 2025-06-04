import os

def criar_diretorios():
    os.makedirs('src', exist_ok=True)
    os.makedirs('bin', exist_ok=True)
    print("📁 Diretórios 'src/' e 'bin/' criados.")

def criar_main_java():
    path_main = os.path.join('src', 'Main.java')
    if not os.path.exists(path_main):
        with open(path_main, 'w') as f:
            f.write("""\
public class Main {
    public static void main(String[] args) {
        System.out.println("Olar mundo!");
    }
}
""")
        print("📝 Arquivo 'Main.java' criado em 'src/'.")
    else:
        print("⚠️ 'Main.java' já existe.")

def criar_gitignore():
    with open('.gitignore', 'w') as f:
        f.write("bin/\n")
    print("📄 Arquivo '.gitignore' criado.")

def criar_readme():
    with open('README.md', 'w') as f:
        f.write("# Projeto Java\n\nEstrutura inicial de projeto Java criada com Python.")
    print("📘 Arquivo 'README.md' criado.")

def instrucoes_uso():
    print("\n✅ Projeto Java inicializado com sucesso!")
    print("""
📌 Próximos passos:

1. Compilar o projeto:
   javac -d bin src/Main.java

2. Executar o projeto:
   java -cp bin Main
""")

def main():
    criar_diretorios()
    criar_main_java()
    criar_gitignore()
    criar_readme()
    instrucoes_uso()

if __name__ == '__main__':
    main()
