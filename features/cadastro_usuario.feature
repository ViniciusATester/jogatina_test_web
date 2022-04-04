@cadastro_usuario
Feature: Cadastrar novo usuário para jogar
  Scenario: Novo cadastro do usuário Vinicius
    Given que acesso o site Jogatina
    When clico no botão cadastre-se
    When preencho o campo "email" e "senha"
    And clico no botão criar conta
    Then sou direcionado para a página de seleção dos jogos
    When clico o incone do perfil e seleciono Ver meu perfil
    Then sou direcionado para página do meu perfil
    When clico em editar informações
    Then sou direcionado para a página de gerenciamento do meu perfil
    When clico em botão editar do campo perfil
    When preencho os campos "cidade" , "estado" , País , sexo e data de nascimento
    And clico no botão alterar perfil
    Then retorno para a página de gerenciamento de perfil


