from utils import present_program, separate_by_line, green
import json
from pathlib import Path

def save_changes(investiments):
    json_investiments = json.dumps(investiments)
    Path("investimentos.json").write_text(json_investiments)

def create_initial_investiments():
    list_of_investiments = [{
        "id": 1,
        "nome": "Câmera",
        "valor": 5000
    },
    {
        "id": 2,
        "nome": "Celular",
        "valor": 4000
    },
    {
        "id": 3,
        "nome": "Maquina de lavar",
        "valor": 2500
    },
    {
        "id": 4,
        "nome": "Tenis",
        "valor": 499
    },
    {
        "id": 5,
        "nome": "Air frayer",
        "valor": 399
    },
    {
        "id": 6,
        "nome": "Moto",
        "valor": 20000
    }
    ]
    json_investiments = json.dumps(list_of_investiments)
    Path("investimentos.json").write_text(json_investiments)

def read_existing_investiments():
    json_investiments = Path("investimentos.json").read_text()
    investiments = json.loads(json_investiments)
    #print(investiments)
    return investiments

def display_total_investiments():
    investiments = read_existing_investiments()
    total = 0
    for investiment in investiments:
        total += investiment["valor"]

    print(f"O total investido até o momento foi de R$:{green(total)}")

def list_investiments(display_all=False):
    from tabulate import tabulate
    investiments = read_existing_investiments()
    investiment_list = []
    if display_all == False:
        for investiment in investiments[0:5]:
            investiment_list.append([investiment["id"],investiment["nome"], investiment["valor"]])
        print(tabulate(investiment_list, headers=["id","nome","valor"]))
    else:
        for investiment in investiments:
            investiment_list.append([investiment["id"],investiment["nome"], investiment["valor"]])
        print(tabulate(investiment_list, headers=["id","nome","valor"]))

def edit_existing_investiments(id_investiment):
    investiments = read_existing_investiments()

    for investiment in investiments:
        if investiment["id"] == int(id_investiment):
            name = input("Informe o novo nome: ")
            value = input("Informe o novo valor: ")
            if name != "":
                investiment.update({"nome": name})
            if value != "":
                investiment.update({"valor": value})

            save_changes(investiments)
            print(investiment)
            return

    print("O ID digitado não existe na nossa tabela! Digite um ID Válido.")
      
def delete_investiment(id_investiment):
    investiments = read_existing_investiments()
    for i, item in enumerate(investiments):
        if item["id"] == int(id_investiment):
            print(f"O investimento {item} foi excluído com sucesso!")
            del investiments[i]
            save_changes(investiments)
    print("O ID digitado não existe na nossa tabela! Digite um ID Válido.")

def get_last_id(investiments):
    last_investiment = investiments[-1:]
    last_id = last_investiment[0]["id"]
    last_id += 1
    return last_id 

def create_new_investiment(name, value):
    investiments = read_existing_investiments()
    last_id = get_last_id(investiments)
    new_investiment = {"id": last_id,"nome": name,"valor": value}
    investiments.append(new_investiment)
    save_changes(investiments)
    print(f"O {new_investiment} Acaba de ser criado!")

def display_menu():
    separate_by_line()
    print("1. Listar investimentos (TODOS)")
    print("2. Editar investimento Existente")
    print("3. Excluir investimento")
    print("4. Criar investimento")
    print("5. Sair")
    option = input("Digite uma opção:")
    separate_by_line()
    return option
    
if __name__ =="__main__":
    present_program()
    while True:
        option = display_menu()
        if option == "1":
            list_investiments(display_all=True)
        if option == "2":
            id_investiment = int(input("Informe o ID do investimento que deseja alterar:"))
            edit_existing_investiments(id_investiment)
        if option == "3":
            id_investiment = int(input("Informe o ID do investimento que desja exlcuir."))
            delete_investiment(id_investiment)
        if option == "4":
            name = input("Nome do novo investimento: ")
            value = int(input("Valor do novo investimento: "))
            create_new_investiment(name, value)
        if option == "5":
            print("Saindo...")
            break