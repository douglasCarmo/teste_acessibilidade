import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from axe_selenium_python import Axe

# URLs corrigidas (removido 'www.' do G1)
sites = {
    "site1_acess.json": "https://www.wikipedia.org",
    "site2_acess.json": "https://www.gov.br",
    "site3_acess.json": "https://g1.globo.com",
    "site4_acess.json": "https://www.amazon.com.br",
    "site5_acess.json": "https://www.github.com"
}

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

try:
    for json_file, url in sites.items():
        print(f"Iniciando varredura em: {url}")
        try:
            driver.get(url)
            
            # Injeta o axe-core e executa a análise
            axe = Axe(driver)
            axe.inject()
            results = axe.run()
            
            # Salva o arquivo JSON
            axe.write_results(results, json_file)
            print(f"Relatório gerado com sucesso: {json_file}\n")
            
        except Exception as e:
            print(f"Falha ao analisar {url}: {e}\n")

finally:
    driver.quit()
    print("Auditoria concluída.")