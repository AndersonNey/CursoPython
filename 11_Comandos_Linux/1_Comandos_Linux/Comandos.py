
#sudo - Permite executar programas c/ privilégios de outro usuário - por padrão, como o root). 
#sudo significa "substitute user do" (usuário substituto faça)



# pwd - print working directory (mostra o caminho do diretório atual)
# ls - lista tudo no diretório atual
#     -a - inclui entradas que o nome começa com ponto (arquivos ou diretórios ocultos)
#     -l - lista em formato longo
#     -h - com -l, é um sufixo de tamanho para facilitar a leitura do tamanho do arquivo
#     -@ - mostra atributos estendidos


#posso concatenar comandos exemplo 

# ls -l -a  (é igual a)  ls -la 
# ls -l -h  (é igual a)  ls -lh


#------------------------------------------------------------------------------------------------------

# cd - change directory
#     .  - diretório atual  (muito util para abrir janela e programas)   ex: open .   (ira abrir uma janela da pasta que voce está)
#     .. - diretório acima
#     /  - o diretório root ou a separação de diretórios
#     ~  - home (cd sem nada vai para a home)
#     - (menos) - volta para o diretório anterior
# tree - mostra a árvore do diretório atual
#     -d - diretórios
#     -a - mostra arquivos ocultos
# cat - concatena e/ou mostra o conteúdo de um arquivo
#     -n - enumera as linhas
# tail - lista as últimas linhas do arquivo
#     -NÚMERO - mostra a quantidade de linhas que for adicionado em NÚMERO.
#     -f - continua assistindo o arquivo em busca de novos dados.   (interessante para ficar vendo arquivos de log que ficam atualizando a todo momento)
# wc - conta linhas, palavras e caracteres
#     -l - linhas
#     -m - caracteres
#     -w - palavras



#Com o comando  cd posso digitar o caminho completo que comeca com a /   (caminho absoluto)
#         ex: cd /home/computador/<ate onde eu queira>
#Com o comando  cd posso digitar o caminho (tipo continuar indo de onde estou(eu sabendo que estou em 'home'))   (caminho relativo)
#         ex: cd computador/<ate onde eu queira>

#com o comando .. posso voltar ate mais pastas
#         ex: cd ../..


#posso criar arquivos com nano e touch 
#              ex: touch nomedoarquivo.txt
#              ex: nano nomedoarquivo.txt



# com o comando 'cat' consigo ler o arquivo no terminal (somente arquivos que ele suporta)
#              ex: cat pasta/nomedoarquivo.txt
# para colocar linhas enumeradas
#              ex: cat -n pasta/nomedoarquivo.txt






# cp - copia arquivos ou diretórios
#     -R - copia o diretório em modo recursivo
#     Obs.: Segundo o man (manual) do cp, se tiver uma barra (/) no final do diretório original, cp pode copiar apenas o conteúdo do diretório e 
#     não o diretório em si (eu não vi isso ocorrer em testes).
# mv - move arquivos ou diretórios (com mv você pode renomear arquivos ou diretórios)
# mkdir - cria um diretório (use aspas ou barra invertida para separar caracteres inválidos)
#     -p - cria uma estrutura inteira sem gerar erros
#     Obs.: você pode usar chaves para criar múltiplos sub-diretórios.
# rm - apaga arquivos e diretórios
#     -R - modo recursivo para diretórios
#     -f - modo forçado e silencioso
# touch - muda os tempos de acesso e modificação de um arquivo. Grande parte dos casos, usamos este comando para criar um arquivo vazio.



