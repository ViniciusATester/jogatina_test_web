@dados_perfil_usuario
Feature: Cadastrar informações do jogador
  Scenario Outline: Com o usuário logado edito as informações do perfil
    Given que acesso o site Jogatina
    When clico no botão entrar e preencho com "<email>" e "<senha>"
    And clico no icone e seleciono ver meu perfil de "<usuario>"
    And sou direcionado para a página do meu perfil e seleciono a opção de editar informacoes
    And sou direcionado para a página de gerenciamento do meu perfil
    And clico em editar no perfil preencho os campos cidade, estado, pais, genero  e nascimento
    And clico no botão alterar perfil e fecho a janela
    Then retorno para a página de gerenciamento de perfil e saio da conta

    Examples:
      | email                       | senha  | usuario                     |
      | viniciustestes05@tester.com | 123456 | viniciustestes05@tester.com |
      | viniciustestes06@tester.com | 654321 | viniciustestes06@tester.com |
