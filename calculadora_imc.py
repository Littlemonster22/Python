def calcular_imc(peso, altura):
    return round(peso / (altura ** 2), 2)

def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 25:
        return "Peso normal"
    elif 25 <= imc < 30:
        return "Sobrepeso"
    elif 30 <= imc < 35:
        return "Obesidade grau 1"
    elif 35 <= imc < 40:
        return "Obesidade grau 2"
    else:
        return "Obesidade grau 3"


def exibir_resultado(imc, classificacao):
    print("\n" + "=" * 40)
    print(f"{'RESULTADO DO CÁLCULO DE IMC':^40}")
    print("=" * 40)
    print(f"IMC: {imc}")
    print(f"Classificação: {classificacao}")
    print("=" * 40 + "\n")


def main():
    print("\n" + "=" * 40)
    print(f"{'BEM-VINDO À CALCULADORA DE IMC':^40}")
    print("=" * 40 + "\n")
    
    while True:
        try:
            peso = float(input("Digite seu peso (em kg): "))
            altura = float(input("Digite sua altura (em metros): "))
    
            if peso <= 0 or altura <= 0:
                print("\nErro: Peso e altura devem ser maiores que zero!")
                continue
            
            if altura > 2.5:
                print("\nErro: Altura inválida! Digite em metros (ex: 1.75)")
                continue
            
            imc = calcular_imc(peso, altura)
            classificacao = classificar_imc(imc)
            exibir_resultado(imc, classificacao)
            
            repetir = input("Deseja calcular novamente? (s/n): ").strip().lower()
            if repetir != 's':
                print("\nObrigado por usar a calculadora de IMC! Até logo!\n")
                break
                
        except ValueError:
            print("\nErro: Digite valores numéricos válidos!\n")
        except Exception as e:
            print(f"\nErro inesperado: {e}\n")


if __name__ == "__main__":
    main()
