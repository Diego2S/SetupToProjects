import os
import subprocess



def criar_venv():
    print("📦 Criando ambiente virtual...")
    subprocess.call(['python3', '-m', 'venv', 'venv'])
    print("✅ venv criada com sucesso!")

    if os.name == 'nt':
        comando = r'venv\Scripts\activate'
    else:
        comando = 'source venv/bin/activate'

    print(f"\n👉 Para ativar a venv, execute no terminal:\n\n   {comando}\n")



def criar_dir():
    os.makedirs('data', exist_ok=True)
    os.makedirs('src', exist_ok=True)
    print("Diretorios criados 'data/' e 'src/' ")

def criar_arq_main():
    path_main = os.path.join('src','main.py')
    if not os.path.exists(path_main):
        with open(path_main, 'w') as w:
            w.write("""
def main():
    print('Olar world!')

if '__main__' == __name__:
    main()""")
            print('main.py criado')
    else:
        print('main.py ja criado')

def criar_requeriments():
    with open('requirements.txt','w') as w:
        w.write('pandas\n')
    print('requeriments.txt criado')


def criar_gitignore():
    with open('.gitignore', 'w') as f:
        f.write("__pycache__/\n*.pyc\ndata/\n")
    print("🗂️ Arquivo '.gitignore' criado.")

def criar_readme():

    with open('README.md', 'w') as f:
        f.write("# Meu Projeto\n\nDescrição inicial do projeto.")
    print("📘 Arquivo 'README.md' criado.")


def instalar_dependencias():
    print("📦 Instalando dependências na venv...")

    if os.name == 'nt':
        pip_cmd = os.path.join('venv', 'Scripts', 'pip.exe')
    else:
        pip_cmd = os.path.join('venv', 'bin', 'pip')

    if not os.path.exists(pip_cmd):
        print("❌ Ambiente virtual não encontrado. Crie a venv antes.")
        return

    subprocess.call([pip_cmd, 'install', '-r', 'requirements.txt'])
    print("✅ Dependências instaladas na venv com sucesso!")


if __name__ == '__main__':
    
    criar_dir()
    criar_arq_main()
    criar_requeriments()
    criar_gitignore()
    criar_readme()
    criar_venv()
    instalar_dependencias()