# REST APIs com Python e Flask
Repositório para estudos de Python com Flask utilizando REST.
Os estudos foram feitos por meio do curso [**REST APIs com Python e Flask**](https://www.udemy.com/course/rest-apis-com-python-e-flask/) e algum conteúdo adicional. Os links serão disponibilizados quando necessário.

## Indice:

1. [Arquitetura REST](#arquitetura-rest)
    * [Quando ela é RESTful](#quando-ela-é-restful)
    * [Vantagens do REST](#vantagens-do-rest)
    * [Diferenças entre API e WebService](#diferenças-entre-api-e-webservice)
    * [Diferenças entre REST e SOAP](#diferenças-entre-rest-e-soap)
    * [REST e HTTP](#rest-e-http)
    * [Collection X Instance](#collection-x-instance)
    * [limit e offset](#limit-e-offset)
    * [O que é CRUD?](#o-que-é-crud)
    * [Métodos HTTP para CRUD](#métodos-http-para-crud)
    * [Status Codes no REST](#status-codes-no-rest)
    * [Como informar ao servidor qual formato de dados enviar como resposta?](#como-informar-ao-servidor-qual-formato-de-dados-enviar-como-resposta)
    * [Autenticação REST](#autenticação-rest)
2. [Python Iniciante](#python-iniciante)
    * [Arrays, Tuplas e Sets](#arrays-tuplas-e-sets)
    * [Laços de iteração e condicionais](#laços-de-iteração-e-condicionais)
3. [Python Avançado](#python-avançado)
    * [List Comprehension](#list-comprehension)
    * [Dicionários](#dicionários)
    * [Classes e Objetos](#classes-e-objetos)
    * [Herança](#herança)
    * [Métodos de Classe e Métodos Estáticos](#métodos-de-classe-e-métodos-estáticos)
    * [args e kwargs](#args-e-kwargs)
    * [Decoradores](#decoradores)

## Arquitetura REST

`REST` (`REpresentational State Transfer`) é um conjunto de `constraints` (regras ou obrigações) criadas para facilitar a transferência de dados, geralmente utilizando o protocolo `HTTP`. `REST` é um estilo arquitetural, ou padrão de projeto (`design pattern`), para `APIs`.

Foi definido por `Roy Fielding`, que a apresentou em sua dissertação de PhD no ano de `2000`.

### Quando ela é RESTful

Para que uma aplicação `seja RESTful`, ela deve seguir `5` das `6` `constraints` definidas a seguir:

1. _Uniform interface_: essa `constraint` tem `4` partes:
    * `Identificação dos recursos`, tipicamente por meio de uma URL (como `api/produtos`, por exemplo);
    * A `resposta` do `servidor` possui informações suficientes para que o `cliente` possa manipular o `recurso` por meio de uma representação (tipicamente, em formato `JSON`);
    * Toda requisição deve ser `auto-descritiva`. Cada `requisição` à `API` contém toda a informação que o `servidor` precisa para o processamento, e toda `resposta` possui toda a informação que o `cliente` precisa para entendê-la;
    * `HATEOAS` (`Hypermedia As The Engine Of Application State`) - modelo que permite que aplicações que usem `APIs REST` naveguem por seus recursos por meio de `links`, tal como o `Hipertexto` de páginas web. A seguir, um exemplo de uma `API` que não segue o modelo `HATEOAS` e outra que segue:
        * **Não segue `HATEOAS`**:
        ```json
            {
                "estados": [
                    {
                        "id": "1",
                        "nome": "Rio de Janeiro",
                        "pais": "Brasil",
                        "times": [
                            {
                                "id": "1",
                                "nome": "Flamengo",
                            },
                            {
                                "id": "2",
                                "nome": "Vasco da Gama",
                            }
                        ]
                    },
                    {
                        "id": "2",
                        "nome": "São Paulo",
                        "pais": "Brasil",
                        "times": [
                            {
                                "id": "1",
                                "nome": "Corinthians",
                            },
                            {
                                "id": "2",
                                "nome": "Palmeiras",
                            }
                        ]
                    }
                ]
            }
        ```
        * **Segue `HATEOAS`**:
        ```json
            {
                "estados": [
                    {
                        "id": "1",
                        "nome": "Rio de Janeiro",
                        "pais": "Brasil",
                        "times": "http://apirest.com.br/api-rest/cidades/1/times"
                    },
                    {
                        "id": "2",
                        "nome": "São Paulo",
                        "pais": "Brasil",
                        "times": "http://apirest.com.br/api-rest/cidades/2/times"
                    }
                ]
            }
        ```
2. _Client-Server Separation_: o `servidor` (`server`) e o `cliente` (`client`) devem agir de maneira independente, interagindo por meio de requisições. O `servidor` deve apenas esperar requisições do `cliente`, não iniciando o envio de informações por si só;
3. _Stateless_: significa que o `servidor` não deve guardar informações sobre o usuário que está usando a `API`. Ele não deve lembrar se o usuário já fez uma requisição (`REQUEST`) para o mesmo recurso ou para quaisquer outros no passado. Em outras palavras, essa `constraint` diz que o servidor não deve guardar dados da `sessão`;
Cada requisição deve conter todas as informações necessárias para realizar o processamento e retornar uma resposta (`RESPONSE`), independentemente de outras requisições feitas pelo mesmo usuário;
4. _Cacheable_: significa que as respostas das requisições deverão conter informações sobre se é ou não possível `cachear` os dados no cliente. Se for possível `cachear` os dados, eles deverão conter uma espécie de versão, pela qual o cliente saberá se está pedindo a mesma informação novamente. O cliente também deverá saber se os dados que possui expirou, e portanto, quando deve solicitá-los novamente;
5. _Layered System_: entre o `cliente` e o `servidor` podem haver `camadas` para prover maior segurança, `load-balancing`, entre outras funcionalidades. Essas camadas não devem afetar a requisição e a resposta, e o `cliente` deve ser agnóstico às camadas utilizadas pelo `servidor`;
6. _Code on Demand (opcional)_: única `constraint` opcional, onde o `cliente` pode requisitar código ao `servidor`, e esse é devolvido geralmente em formato script (como no formato `javascript`) para ser executado no próprio `cliente`.

Mais em:
- https://www.youtube.com/watch?v=ghTrp1x_1As
- https://www.youtube.com/watch?v=M5NWpt5d59E
- https://medium.com/extend/what-is-rest-a-simple-explanation-for-beginners-part-1-introduction-b4a072f8740f
- https://medium.com/extend/what-is-rest-a-simple-explanation-for-beginners-part-2-rest-constraints-129a4b69a582
- https://medium.com/@mellomatheuslima/a-import%C3%A2ncia-do-hateoas-em-apis-restful-1ca2dc081288


### Vantagens do REST

* O `servidor` e o `cliente` podem evoluir de forma independente;
* Pode haver mais de uma versão do `cliente` (como `mobile` e `web`) e ambas acessarão o mesmo `servidor`;
* Sendo `Stateless`, faz com que as `requisições` sejam mais transparentes por conterem as informações necessárias para o processamento;
* Sendo `Cacheable`, diminui a latência entre as requisições, já que parte das `requisições` serão `cacheadas` pelo `cliente`;

### Diferenças entre API e WebService

`API (Application Programming Interface)`: é como uma ponte (`interface`) entre dois programas - um canal de comunicação para envio de informações. Uma analogia: é como, em um restaurante, o garçom, que é quem recebe o pedido do cliente e leva até a cozinha. Quando pronto o pedido, o garçom traz o prato (resultado) da cozinha até o cliente. É uma forma que terceiros utilizam para a disponibilização de seus serviços, sem que precisemos nos preocupar com sua implementação.

`WebService`: é uma `API` projetada para se comunicar obrigatoriamente via `rede`. Tipicamente, usa o protocolo `HTTP` para comunicação. Utilizam `SOAP`, `REST` ou `XML-RPC` como meio de comunicação.

### Diferenças entre REST e SOAP

Algumas diferenças:

 | * | `REST` | `SOAP` |
| --- | --- | --- |
| Protocolos suportados | `HTTP` / `HTTPS` | Pode ser usado com a maioria dos protocolos (incluindo `HTTP`, `SMTP`, `TCP` e `JMS`) |
| Formatos de resposta | `CSV`, `JSON`, `XML`, `YAML`, entre outras | `XML` |


Mais em:
- http://www.matera.com/blog/post/rest-usa-json-e-soap-usa-xml-certo

### REST e HTTP

No `HTTP (Hyper Text Transfer Protocol)` é, literalmente, um Protocolo para Transferência de Hipertextos. O hipertexto mais conhecido é o `HTML` (`Hyper Text Markup Language`). Quando clicamos em um link, na verdade, estamos fazendo uma requisição utilizando o método `GET` do protocolo `HTTP`. No envio de formulários, a requesição é com o método `POST`. Ao fazer uma requisição para um `WebService` `REST`, no entanto, obtemos somente dados - e não páginas web.

### Collection X Instance

Uma `URI` com um recurso único chama-se instância (`Instance`), enquanto um `URI` com vários recursos chama-se coleção (`Collection`).

```
    /postagens      => coleção
    /postagens/{id} => instância
```

> Para uma coleção, use um `substantivo` no `plural` como boa prática.

### limit e offset

Podemos usar `limit` para indicar, na `URI`, o número máximo de items a serem retornados. Já `offset` pode ser usado para pular uma quantidade de items da listagem na base de dados.

```
    /postagens?limit=10&offset=30
```

> Embora limit e offset sejam utilizados por padrão, podemos criar outros parâmetros de busca, tais como `ano` e `tipo`.

### O que é CRUD?

Acrônimo para `Create`, `Read`, `Update` e `Delete` - 4 operações básicas de um cadastro.

### Métodos HTTP para CRUD

Podemos relacionar os métodos HTTP da seguinte forma com um CRUD:

| Ação CRUD | Método HTTP |
| --- | --- |
| Create | `POST` |
| Read | `GET` |
| Update | `PUT` |
| Delete | `DELETE` |

### Status Codes no REST

`Status Codes`: são códigos enviados em conjunto com a resposta de uma requisição `HTTP`. Esses códigos ajudam a validar se uma requisição foi bem sucedida, e caso contrário, a verificar qual foi o tipo do erro.

Alguns exemplos:

| Status Code | Tipo | Explicação |
| --- | --- | --- |
| 200 | Success | Esta requisição foi bem sucedida. |
| 400 | Bad Request | Essa resposta significa que o servidor não entendeu a requisição pois está com uma sintaxe inválida. |
| 401 | Unauthorized | Embora o padrão `HTTP` especifique _unauthorized_, semanticamente, essa resposta significa _unauthenticated_. Ou seja, o cliente deve se autenticar para obter a resposta solicitada. |
| 403 | Forbidden | O cliente não tem direitos de acesso ao conteúdo portanto o servidor está rejeitando dar a resposta. Diferente do código `401`, aqui a identidade do cliente é conhecida. |
| 404 | Not Found | O servidor não pode encontrar o recurso solicitado. Este código de resposta talvez seja o mais famoso devido à frequência com que acontece na web. |
| 412 | Precondition Failed | O cliente indicou nos seus cabeçalhos pré-condições que o servidor não atende. |
| 500 | Server Error | O servidor encontrou uma situação com a qual não sabe lidar. |

Mais em:
- https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Status


### Como informar ao servidor qual formato de dados enviar como resposta?

Para informar ao servidor qual o formato de dados enviar como resposta, devemos acrescentar um cabeçalho  (`Header`) na requisição chamado `Content-Type`. Cabeçalhos podem conter metadados (`Metadata`) que podem ser usados pelo servidor como informação adicional, como é o caso de `Content-Type`.

> Para a resposta ter o formato `JSON`, devemos enviar o cabeçalho `Content-Type` com o valor `application/json`.

### Autenticação REST

A autenticação em uma arquitetura convencional geralmente se dá da seguinte forma:

1. O cliente envia uma requisição com o seu usuário e senha;
2. O servidor valida essas informações e, em caso positivo, envia um `token` da sessão;
3. O cliente geralmente guarda o `token` como `cookie`;
4. Em toda requisição posterior, o cliente envia o `token` como sinal de que está autenticado;
5. Quando o cliente não deseja mais continuar autenticado, informa o servidor, que destroi o `token` e a sessão.

No entanto, em uma arquitetura `REST`, isso é um problema, pois ela é `Stateless` e portanto, não mantém dados da sessão.

Para resolvermos esse problema, o mecanismo de autenticação mais básico se chama `Basic Auth` (`Basic Auth Authentication`). Ele funciona com o cliente enviando seu usuário e senha em todas as requisições, por meio do `Header` `Authorization`, onde **ambos serão codificados** utilizando o algoritmo `Base64`. O código resultante é enviado como conteúdo do cabelho `Authorization` após a palavra `Basic `, como segue o exemplo:

| Header | Value |
| --- | --- |
| Authorization | Basic dXN1YXJpbzpzZW5oYQ== |

> **Codificação não é criptografia**. Logo, qualquer um que tenha acesso à essa string codificada pode decodificá-la com `Base64`. Portanto, a codificação feita somente com `Base64` **não é segura**. Portanto, quando se usa `Basic Auth`, deve-se fazê-lo com `HTTPS`. O motivo pelo qual codificamos os caracteres é que alguns deles não são compatíveis com `HTTP`.

Vantagens do `Basic Auth`:

* Simples;
* Stateless;
* Suportado por todos os browsers.

Desvantagens do `Basic Auth`:

* Apenas `HTTPS`;
* Sujeito a ataques (já que os dados de usuário e senha são enviados o tempo todo);
* Deslogar pode ser um processo complicado.

Melhores soluções:

* Digest Access Authentication;
* Asymmetric Cryptography;
* OAuth;
* JSON Web Token.

## Python Iniciante

`Python` é uma linguagem crida por `Guido van Rossum` em `1991` com foco em **produtividade** e **legibilidade**. É muito utilizada para fins acadêmicos e científicos por sua incrível facilidade de leitura e uso.

Entre suas principais características estão:

* Uso de identação para marcar blocos (`4` espaços para cada identação);
* Coletor de lixo (`Garbage Collector`) para gerenciamento automático da memória;
* Suporte a multiplos paradigmas de programação.

Como a identação é usada para definir blocos (como em funções e em laços de iteração), códigos feitos fora desse padrão causarão falhas na execução de programas. A vantagem disso é que todo código escrito na linguagem segue um padrão, o que facilita a leitura de códigos escritos por outras pessoas. A desvantagem é que isso força o programador a seguir esse padrão. Exemplos:

O código a seguir está correto:
```python
def metodo:
    print("olá mundo")
```

Já o código a seguir está incorreto, e portanto, causará um erro:
```python
def metodo:
print("olá mundo")
```

Comentários em `Python` são descritos utilizando o caractere `#`:

```python
# comentário qualquer
```

Mais em:
- https://www.python.org/dev/peps/pep-0008/
- http://pyscience-brasil.wikidot.com/python:python-oq-e-pq

### Arrays, Tuplas e Sets

`Arrays` são, como em outras linguagens, definidos entre colchetes:

```python
arrayTeste = [1,10]
```

Podemos adicionar valores por meio do método add:

```python
arrayTeste.add(20)
```


`Tuplas` tem um funcionamento parecido com os `arrays`, mas tem seu conteúdo fixo (isso é, não podemos adicionar elementos nela) e são definidas por meio de parênteses:

```python
tuplaTeste = (1,10)
```

Por fim, `sets` também são parecidos com `arrays`, podemos adicionar valores também pelo método `add()`, mas seus valores não podem ser duplicados. Valores duplicados serão ignorados. Também não tem indexação de seus valores, o que significa que no `set` `valores`, `valores[0]` não é permitido. São definidas por meio de chaves:

```python
setTeste = {1,10}
```

### Laços de iteração e condicionais

Para comparar ou iterar estruturas e variáveis em `Python`, usamos os seguintes operadores:

| Símbolo | Definição |
| --- | --- |
| `==` | Igual |
| `!=` | Diferente |
| `>` | Maior que |
| `<` | Menor que |
| `>=` | Maior ou igual que |
| `<=` | Menor ou igual que |

Podemos usar estruturas condicionais (`if` e `else`) utilizando operadores ou utilizando a palavra-chave `in` para verificar se há um conteúdo em uma lista:

```python
nome = "Jose"
lista = ["Joao", "Pedro", "Jose"]

if nome == "Jose":
    print(f"<nome> == Jose")
else:
    print(f"<nome> != Jose")


if nome in lista:
    print(f"{nome} esta em <lista>")
else:
    print(f"{nome} nao esta em <lista>")

```

Também podemos utilizar a palavra-chave `in` em laços do tipo `for` para iterar em todos os itens de uma lista. Podemos usar os todos os operadores tanto em laços do tipo `for` quanto em laços do tipo `while`:

```python
lista = ["Joao", "Pedro", "Jose"]

for nome in lista:
    print(f"Nome na lista: {nome}")

# a função len() conta o número de items em uma lista qualquer, ou o número de caracteres em uma string
while len(lista) >= 1:
    # o método pop() retira e retorna um elemento de uma lista
    elemento = lista.pop()
    print(f"Retirando o elemento {elemento} da lista")

```

> A partir do `Python 3.6` foi adicionada `interpolação de strings`. Para isso, precisamos usar strings do tipo `formatted string literals` (ou `f-strings`) que são definidas com um `f` antes das aspas. Assim, podemos usar `{variável}` para realizar a interpolação das `strings`.

Mais em:
- https://www.devmedia.com.br/estruturas-de-condicao-e-repeticao-em-python/37158
- https://realpython.com/python-string-formatting/


## Python Avançado

### List Comprehension

`List Comprehension` é uma maneira de filtrar o conteúdo de uma lista utilizando uma `notação` da seguinte forma:

```python
content = [x for x in iteravel]

# também podemos retornar a List Comprehension em um set
contentSet = {x for x in iteravel}

```

Adicionalmente, podemos incluir `condicionais` à `notação`, como a seguir, onde queremos apenas números maiores de 30:

```python
lista = [20,30,40,50,60,70]

resultado = [x for x in lista if x > 30]

# resultado = [40,50,60,70]

```

Podemos também modificar o valor de `x` para cada valor utilizando um operador. A seguir, multiplicamos cada valor por `2` em valores que sejam maiores que `20`:

```python

lista = [10,20,30,40,50]

resultado = [x * 2 for x in lista if x > 20]

# resultado = [60, 80, 100]

```

Um exemplo do uso de `List Comprehension` é a correção de caixa e espaços em uma lista de nomes:

```python
listaNomes = ['   JoÃO', '   CaRlOS   ', '   MichEL ']

# strip() retira espaços e capitalize() altera somente o primeiro caractere para maiúsculo,
# deixando os outros em minúsculo
listaFiltrada = [nome.strip().capitalize() for nome in listaNomes]

# listaFiltrada = ['João', 'Carlos', 'Michel']
```

### Dicionários

Um `dicionário` é definido por meio de um conjunto de dados definidos no formato `chave-valor`. Sua definição é muito parecida com a de um `JSON`, onde cada valor é acessado por sua chave:

```python

dicionario = { 'chave': 'valor', 'nome': 'joao' }

# dicionario['chave'] = 'valor'
```

`Dicionários` também podem ser comparados em relação ao seu conteúdo:

```python
dic1 = { 'id': 1 }
dic2 = { 'id': 1 }

if dic1 == dic2: # true
    print('Os dicionários possuem o mesmo conteúdo.')

```

### Classes e Objetos

Enquanto a `Classe` é um modelo abstrato de um conjunto de dados, descrevendo o acesso de seus atributos como `publicos` ou `privados`, um `Objeto` é uma instância de uma `Classe`. Isso significa que, enquanto a `Classe` descreve o comportamento de uma entidade, ela não é usada diretamente no processamento de nossa aplicação - e sim os `Objetos`, que são unidades alocadas em memória para uso a partir de `Classes` definidas. Em outras palavras, é como se a `Classe` fosse a planta de uma casa, enquanto o `Objeto` fosse a própria casa já construída.

Uma `Classe` é definida da seguinte forma:

```python

class Casa:
    def __init__(self, rua, numero):
        self.__rua = rua
        self.__numero = numero

    def enderecoCompleto(self):
        return f"{self.__rua}, {str(self.__numero)}"

```

Aqui, podemos ver alguns detalhes:
- O primeiro parâmetro de todos os métodos aponta para a própria instância - isso é, serve para acesssar as propriedades do próprio objeto. Por padrão, nomeamos `self`;
- `def __init__(self, [variaveis])` é o método construtor da `Classe`. É chamado sempre que se instancia um novo `Objeto`;
- As variáveis `privadas` são precedidas por `__`. Por padrão, essas variáveis sofrem `mangle`, podendo ser acessadas por _NomeDaClasse__variavel, embora o acesso externo seja desencorajado.

Para exemplificar, é assim que a `classe` **Casa** deve ser instanciada: 

```python

casa1 = Casa("Nome da rua", 100)

# abaixo, uso do método enderecoCompleto() da classe
print(casa1.enderecoCompleto())

```

Diferente dos `dicionários`, não podemos comparar os conteúdos de duas instâncias de uma mesma `Classe`, mesmo que contenha o mesmo conteúdo. Assim:

```python
casa1 = Casa("teste", 100)
casa2 = Casa("teste", 100)

if casa1 == casa2:
    print("TRUE")
else:
    print("FALSE")

# retorna FALSE

```

### Herança

`Classes` filhas possuem as características da `Classe` pai.

Para exemplificar:

```python

class Funcionario:
    def __init__(self, nome, salario):
        self._nome = nome
        self._salario = salario

    def dados(self):
            return {'nome': self._nome, 'salario': self._salario}

class Admin(Funcionario):
    def __init__(self, nome, salario):
        super().__init__(nome, salario)

    def atualizarSalario(self, salario):
        self._salario=salario

    def atualizarNome(self, nome):
        self._nome=nome
```

No exemplo, a `classe` **Admin** herda as características da `classe` **Funcionario**. Para isso, basta passar como argumento a `classe` _pai_ na criação da `classe` _filha_. Dessa forma, os `objetos` instanciados a partir de **Admin** terão mais dois métodos: `atualizarSalario()` e `atualizarNome()`, e ainda poderão acessar o método dados(), definido na `classe` _pai_. A `classe` **Funcionario**, no entanto, continuará apenas com as funcionalidades definidas em sua própria estrutura.

É importante notar, dentro do método `__init__()` de **Admin**, uma chamada ao método `super()`. Esse método permite acesso aos métodos da `classe` _pai_. Assim, **Admin** chama **__init__()** da `classe` _pai_, não sendo necessário redefiní-lo.

As variáveis possuem apenas um `underline` (`_`) pois essa é a convenção, em `Python`, para variáveis `protected` - isso é, acessível apenas na própria `classe` ou em suas _filhas_.

> `Python` não possui **palavras-chave**  para definir acessos `publicos`, `privados` ou `protegidos` em `classes`. Essas definições são feitas por **convenção**, onde `_` é utilizado para acessos `protegidos` e `__`  para privados. Onde não há underscore, o acesso é `público`.

### Métodos de Classe e Métodos Estáticos

`Métodos de Classe` e `Métodos Estáticos` são definidos por meio de `decoradores` (`decorators`) embutidos na linguagem.

`Métodos de Classe` são definidos por meio do decorador `@classmethod` e sempre recebem como primeiro parâmetro uma referência para a própria classe (**e não para suas instâncias**) que, por convenção, chamamos de `cls` ( de `classe`). Tem ligação com a `classe`, e não com suas `instâncias` (o que nos faz chamá-los por meio do nome da pŕopria `classe`).

Alterações feitas por meio de `Métodos de Classe` são refletidas em todas as `instâncias`. Geralmente, usamos esses métodos para criar `métodos factory` (` factory methods`):


```python
class Funcionario:
    __aumento = 1.00
    __salarioPadrao = 1000

    def __init__(self, nome, salario):
        self._nome = nome
        self._salario = salario

    def dados(self):
            return {'nome': self._nome, 'salario': self._salario}

    def aplicarAumento(self):
        self._salario = self._salario * self.__aumento

    @classmethod
    def definirNovoAumento(cls, aumento):
        cls.__aumento = aumento

    @classmethod
    def comSalarioPadrao(cls, nome):
        return cls(nome, cls.__salarioPadrao)



funcionario1 = Funcionario("Guilherme", 1000)
funcionario2 = Funcionario.comSalarioPadrao("Carlos")

# chamada ao método de classe
Funcionario.definirNovoAumento(1.10)

funcionario1.aplicarAumento()
funcionario2.aplicarAumento()

print("Dados do funcionário #01: ")
print(funcionario1.dados())
print("Dados do funcionário #02: ")
print(funcionario2.dados())

# ambos os funcinonários atualizaram seus salários para 1100

```

`Métodos Estáticos` são ligados à `classe`, e não às `instâncias` dela. Não possuem referência nem à `classe`, nem às suas `instâncias` - portanto, não podem acessar ou modificar o estado da `classe`.

São usados, geralmente, para criar métodos utilitários:

```python
class Contrato:
    @staticmethod
    def paisesPermitidos():
        return ['Brasil', 'Espanha', 'Portugal']

```

Mais em:
- https://www.geeksforgeeks.org/class-method-vs-static-method-python/


### args e kwargs

De forma resumida:
* `args`: são argumentos em quantidade não definida , processados em formato de `tupla`;
* `kwargs`: são `keyword arguments` (argumentos de palavras-chave) em quantidade não definida, processados em formato de `dicionário`;

`args` são definidos com **um asterisco**, usados como multiplos argumentos e processados como uma `tupla`:

```python

def soma(*args):
    return sum(args)

soma(1,2,3)
# 6

```

`kwargs` são definidos com **dois asteriscos**, usados como um conjunto de _chave-valor_ (x=valor, y=valor2, etc) e processados em formato de `dicionário`:

```python

def informaNome(**args):
    if 'nome' in args:
        print(f"Nome informado: {args['nome']}")
    if 'sobrenome' in args:
        print(f"Sobrenome informado: {args['sobrenome']}")

informaNome(nome="Pedro")
# Nome informado: Pedro

```

### Decoradores

`Decoradores` (ou `decorators`) são ferramentas muito poderosas na linguagem `Python`, pois permitem que modifiquemos o comportamento de `funções` e `classes`. `Decoradores` nos permitem criar um `wrapper` por meio de outra `função`, para assim estendermos o comportamento da `função` original.

Nos `decoradores`, a _função principal_ é passada como o primeiro argumento para _outra função_, e então processada dentro desta função:

```python
import time

# definição de decorator para calcular duração entre inicio e final da função
def calcula_duracao(funcao):
    def wrapper(*args, **kwargs):
        tempo_inicial = time.time()
        funcao(*args, *kwargs)
        tempo_final = time.time()
        tempo_execucao = tempo_final - tempo_inicial

        print(f"[{funcao.__name__}] Tempo de execução: {tempo_execucao}")

    return wrapper

@calcula_duracao
def soma(num1, num2):
    print(f"Soma de números: {num1+num2}")

soma(1,2)

# informa tempo de execução do método ao final no fomato: [soma] Tempo de execução: [tempo]


```

Para utilizar parâmetros em um `decorador`, pode-se incluir uma `função` adicional à declaração, onde será recebido como parâmetro esse novo argumento:

```python
def multiplica_valor(valor):
    def internal(funcao):
        def wrapper(*args, **kwargs):
            return funcao(*args, *kwargs) * valor
        
        return wrapper

    return internal

@multiplica_valor(2)
def soma(num1, num2):
    return num1+num2

print(f"Soma de números (x2): {soma(1,2)}")

# resultado: 6
```

Pode-se perceber que, com passagem de parâmetros, cria-se um novo _"nível"_ de execução para receber esses parâmetros - por isso, a necessidade de uma nova `função`.

Um `decorador` também pode ser definido no formato de `classe`. O método `__init__()` receberá, nesse caso, a função como segundo parâmetro, e iremos utilizar o método `__call__()` para realizar o `wrap` - e para isso, receberá os parâmetros da função decorada:

```python
from time import time 

class Timer:
    def __init__(self, func): 
        self.function = func 
  
    def __call__(self, *args, **kwargs): 
        inicio = time() 
        retorno = self.function(*args, **kwargs) 
        fim = time() 
        print(f"A execução durou {format(fim-inicio)} segundos") 
        return retorno 
  
@Timer
def funcao_teste(delay): 
    from time import sleep 
  
    # delay usado para simular tempo de processamento
    sleep(delay) 
  
funcao_teste(3) 

```

 Caso se queira ter parâmetros no `decorador`, deve-se adicionar uma função adicional ao método `__call__()`. Nesse caso, `__init__()` receberá os parâmetros do `decorador` a partir do segundo parâmetro, `__call__()` receberá a `função` como segundo parâmetro, e o método adicional em `__call__()` receberá os parâmetros da função decorada: 

 ```python
 class DivideValor:
  
    def __init__(self, valor): 
        self.valor = valor
  
    def __call__(self, function):

        def wrapper(*args, **kwargs):
            result = function(*args, **kwargs) / self.valor
            return result

        return wrapper

@DivideValor(2)
def soma(num1, num2):
    return num1+num2

print(f"Soma de números (/2): {soma(2,4)}")
# retorna 3

 ```

> Podemos adicionar mais de um `decorador` à uma `função` ou `classe`. Nesse caso, a execução será feita de baixo para cima.

Mais em:
- https://www.geeksforgeeks.org/decorators-in-python/
- https://dev.to/apcelent/python-decorator-tutorial-with-example-529f
- https://www.geeksforgeeks.org/decorators-with-parameters-in-python/
- https://www.geeksforgeeks.org/class-as-decorator-in-python/
- https://www.codementor.io/dobristoilov/python-class-decorator-part-ii-with-configuration-arguments-rv73o8pjn