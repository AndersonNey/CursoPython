# https://gist.github.com/luizomf/6a57d2c7f93624ea92fe1c3bc8f7243b

#https://www.todoespacoonline.com/w/2015/06/usuarios-grupos-e-permissoes-no-linux-ubuntu/



# sudo adduser nome_do_usuario    #Para criar um usuario  (lembrando que ele vem com permissoes padroes))(e quando se cria um usuario tambem é criado um grupo de mesmo nome)
# sudo deluser nome_do_usuario    #Para remover o usuario
# sudo password nome_do_usuario   #caso esqueca a senha do usuario
# sudo login                      #login para logar com algum usuario  (ele pergunta depois qual o usuario e a senha)
# logout                          #para sair 


# sudo addgroup nome_do_grupo     #para criar um grupo
# sudo delgroup nome_do_grupo     #para excluir um grupo
# sudo adduser nome_do_usuario nome_do_grupo   #adicionando determinado usuario ao um determinado grupo     (EX:sudo adduser nome_do_usuario sudo     #adicionando o usuario ao grupo sudo)
# sudo deluser nome_do_usuario nome_do_grupo   #removendo determinado usuario de um determinado grupo

# cat /etc/group                  #vendo os grupos existentes
# grep nome_do_grupo /etc/group   #vendo o grupo especifico (e quem esta presente nele)
# cat /etc/passwd                 #vendo os usuarios existentes (todos os usuarios sao gravados no arquivo /etc/passwd)
# grep nome_do_usuario /etc/passwd       #vendo um usuario especifico


#PERMISSOES

#sao 3 tipos de permissoes  (read , write , execute) rwx   e quando nao tem permissao (nao tem permissao) - "onde nao tem permissao nao soma"

# 421 = 7     421 = 5     421 = 4     421 = 0
# rwx         r-x         r--         ---



#Exemplo que irei trabalhar:
#
# -rw-r--r-- 1 computador computador 639 ago 31 13:33 index.html
#

#O primeiro caracter representa ((-) arquivo ou (d) diretorio)
# Proprietario , grupo , todos   (rw-r--r--)
# representa links (1)
# proprietario da pasta (computador)
# grupo que essa pasta esta (computador)
# tamanho   (639)
# ultima data que foi modificado (ago 31 13:33)
# nome com a extensao (index.html)  caso fosse pasta so seria o nome

#ainda seguindo o exemplo anterior 

#  421 = 6   421 = 4   421 = 4
#  rw-       r--       r--

#MODIFICANDO AS PERMISSOES

# sudo chmod novo_numero_que_representa_as_permissoes_do(Proprietario , grupo , todos )     #alterando as permissoes do arquivo
#          # ex:   sudo chmod 700 nome_do_arquivo

# sudo chmod novo_numero_que_representa_as_permissoes_do(Proprietario , grupo , todos )     #alterando as permissoes de varios arquivos dentro de uma pasta
#          # ex:   sudo chmod 700 nome_da_pasta/ -R
#esse R é de recursivo ,ou seja , faca isso para tudo que estiver dentro da pasta

# sudo chmod novo_numero_que_representa_as_permissoes_do(Proprietario , grupo , todos )     #alterando as permissoes da pasta   (somente da pasta ,arquivos dentro nao sao alterados)
#          # ex:   sudo chmod 700 nome_da_pasta


#NAO TESTADOS DE FATO

#MODIFICANDO O PROPRETARIO

# sudo chown nome_do_novo_usuario nome_do_arquivo    #para um arquivo especifico
# sudo chown nome_do_novo_usuario nome_da_pasta/ -R  #para varios arquivos dentro de uma pasta
# sudo chown nome_do_novo_usuario nome_da_pasta      #para uma pasta especifica

#MODIFICANDO O GRUPO

# sudo chgrp nome_do_novo_grupo nome_do_arquivo    #para um arquivo especifico
# sudo chgrp nome_do_novo_grupo nome_da_pasta/ -R  #para varios arquivos dentro de uma pasta
# sudo chgrp nome_do_novo_grupo nome_da_pasta      #para uma pasta especifica





#Para escapar espaços
# ex: Python para testes

#     /Python\ para\ testes







