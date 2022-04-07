##Teste web - Desafio Gazeus

A linguagem escolhida foi o Python, por maior afinidade no momento
e o framework utilizado foi o Selenium Webdriver para a execução dos testes web.

###Preparação do ambiente

 As ferramentas utilizadas estão para execução do código são:

 -Python 3 , seu download pode ser acessado em <https://www.python.org/>

 -IDE utilizada foi o PYCHARM da JetBrains, mas podendo ser outra de sua preferência
 
-Baixar o arquivo via link abaixo:

<https://github.com/ViniciusATester/jogatina_test_web>

 -Deverá instalar os plugins e fazer importações 
 * Cucumber
 * behave
 * pytest
 * Selenium, webdriver e demais classes

Podem ser feitas as instalações através do arquivos requirements, pelo Python Packages
diretamente no terminal com comando pip install (pluglin), diretamente no código e pelo 
comando Ctrl+Alt+S na aba de plugins e pesquisando pelo nome.

Descrição do teste automatizado:
Foi utilizado a técnica de BDD e para 
Dentro da propria codificação, encontrará comentários que auxiliam o entendimento do mesmo,
como validações de textos, imagens, e campos.



Para executar as features:

Selecionar o terminal digitar behave e pressionar Enter, ele executará todas as features.
para selecionar uma feature precisará digita behave -i (nome da feature) e pressionar Enter.
 
EX: behave -i cadastro_usuario.feature

OBS: Foram utilizados alguns pontos como alfinetes que são as esperas forçadas através
dá classe time com o comando time.sleep(), seu que o certo é apagar para poder enviar
a um cliente quando é o caso. Mas deixarei os comandos todos comentário, caso alguma parte do código 
trave ou algo do tipo, pois minha máquina já é um pouco fraca para rodar então fica difícil sicronizar os testes.
Dito isto também ressalto a possui uma esperado implicita dentro da estrutura de abertura
e fechamento do browser, o que deveria ser o suficiente para conclusão dos testes, 
mas precisei usar o recurso do time.sleep() para rodar como expliquei acima.



    
 