Projeto Setup Automático — Python & Java

Este projeto contém scripts em Python para criar automaticamente a estrutura básica de projetos nas linguagens Python e Java, facilitando o início rápido de desenvolvimento.

Para projeto Python

    Execute o script:

    python3 setup_python.py
    python3 setup_java.py

Estrutura gerada

Python
.
├── data/
├── src/
│   └── main.py
├── requirements.txt
├── venv/
├── .gitignore
└── README.md

Java
.
├── src/
│   └── Main.java
├── bin/
├── .gitignore
└── README.md


Observações

    Os scripts não sobrescrevem arquivos existentes.

    O arquivo .gitignore ignora arquivos temporários e diretórios de build/venv.

    O requirements.txt inicial inclui a biblioteca pandas como exemplo.

Contato

Desenvolvido por Diego2S.