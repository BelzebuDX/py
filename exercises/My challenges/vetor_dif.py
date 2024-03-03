vet1 = input(
    "Digite uma sequencia de numeros para o primeiro vetor: ").split(" ")
vet2 = input(
    "Digite uma sequencia de numeros para o segundo vetor: ").split(" ")
vet_final = []
for i in range(len(vet1)):
    if vet1[i] not in vet2:
        vet_final.append(vet1[i])
    else:
        continue

print(f"o vetor final da diferença é: {vet_final}")
