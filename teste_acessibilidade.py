from selenium import webdriver
from axe_selenium_python import Axe

# 1. Inicializa o navegador (Ex.: Acessar o Chrome)
driver = webdriver.Chrome()

try:
    # 2. Definir a URL que será testada
    url = "https://www.google.com"
    driver.get(url)

    # 3. IUnstaciar a ferramenta Axe e injetar os testes na página
    axe = Axe(driver)
    axe.inject()

    # 4. Executar a verificação de acessibilidade
    results = axe.run()

    # 5. Salva os resultados das violações encontradas em um arquivo JSON
    axe.write_results(results,"resultado_acessibilidade.jdson")

    # Exibir no terminal a quantidade de violações encontradas
    violations = results.get("violations", [])
    print(f"Testes concluidos! Violações encontradas: {len(violations)}")

finally:
    # 6. Encerrar a sessão do navegador
    driver.quit()