precoOriginal = float(input('digite o preço original do produto: R$'))

percentualDesconto = int(input('digite a porcentagem de desconto:'))

valorDesconto = precoOriginal * (percentualDesconto/100)

precoComDesconto = precoOriginal - valorDesconto

print('preço original: R$' , precoOriginal)
print('desconto:' , percentualDesconto,'%')
print('preço com desconto: R$' , precoComDesconto) 


