# CSS - The Complete Guide: Anotações do curso

## Seção 2

> Combinators: Siblings em CSS

Há quatro tipos de `combinadores` para `seletores` em `CSS`:

Os `combinators` (combinadores) definem estilos a partir de uma combinação, onde o estilo é aplicado no último elemento indicado. Por exemplo, em `div > a { color: blue }`, o estilo será aplicado no elemento `<a>` filho de `<div>`. Abaixo, mais detalhes sobre as possíveis combinações:

- `adjacent siblings` (irmãos adjacentes): é feito ao somar seletores (dois ou mais), por meio de um sinal de soma (`+`), como em `div + a {}`. O  estilo, nesse caso, é aplicado somente quando os dois seletores são dispostos sequencialmente no `HTML`, um após o outro. Os elementos precisam estar no mesmo nível;
- `general siblings` (irmãos genéricos): nesse caso, os estilos serão aplicados da mesma forma que a combinação acima, exceto que os elementos não precisam necessariamente estar dispostos diretamente um após o outro. Pode ser que, por exemplo, um outro elemento esteja entre esses dois elementos. Ainda assim, os estilos serão aplicados no último elemento indicado. Essa combinação é feita por meio de um til (`~`): `div ~ a {}`;
- `child` (filho): nesse caso, o estilo será aplicado no elemento filho. Para que seja aplicado, o elemento filho deverá estar contido diretamente no pai - isso é, caso a distância seja de mais de um nível, o estilo não será aplicado. Essa combinação é feita com um sinal de maior (`>`): `div > a {}`;
- `descendant` (descendente): nesse caso, todos os elementos que estiverem contidos no elemento pai terão o estilo aplicado. Essa combinação é feita somente com um espaço entre os seletores. Por exemplo, em `div a {}`, o estilo será aplicado em todos os elementos do tipo `<a>` filhos de um elemento `<div>`.

**Observação:** Não se trata exatamente de `combinators`, mas é possível criar estilos para um elemento de forma mais precisa indicando diretamente as `classes` ou `identificadores` contidos nesse elemento. Para isso, deve-se usar o nome do `elemento` e da(o) `classe/identificador` juntos, sem haver espaços entre eles, como em `div.classe {}` ou `a#nome {}`.

## Seção 3

> box-sizing do tipo border-box e content-box

Quando definimos a propriedade `width` de um `elemento`, o calculo da largura é feito de formas distintas de acordo com a configuração da propriedade `box-sizing` desse elemento. Podemos citar dois tipos:
- `content-box`: geralmente definido por padrão, o calculo do `width` nesse caso é baseado somente no conteúdo, sem levar em consideração as propriedades `border` e `padding`;
- `border-box`: quanto definido como `border-box`, o calculo é feito levando em consideração as propriedades `border`, `padding` e `margin`, o que pode facilitar na definição das propriedades do elemento.

> Elementos `inline`, `block`, e `inline-block`

De certa forma, todos os elementos na tela do **browser** são renderizados em caixas retangulares. Dependendo da propriedade `display` de cada objeto, essas caixas podem ocupar o espaço de renderização de maneira diferente por meio dos tipos `block` e `inline`.

De forma resumida e direta, elementos do tipo `block` (`display: block`)  ocupam uma linha inteira de determinada porção da página. Por isso, são utilizados com elementos do tipo `div`, `header` ou `p`, já que são tipos que compõem blocos maiores.

Elementos do tipo `inline` compõem apenas o espaço necessário para seu próprio conteúdo - portanto, podem ser apresentados seguidamente, um do lado outro. Eles tem algumas restrições de estilo - os estilos `margin-top` e `margin-bottom` não são aplicáveis sobre eles. Elementos do tipo `inline` podem iniciar em uma linha de texto, e terminar em outra.

Ainda existe um terceiro tipo chamado `inline-block`, o qual possui características dos dois tipos citados, mantendo o comportamento do tipo `inline`, mas com as possibilidades de customização de estilo disponibilizadas pelo tipo `block`.


Mais em: 
- https://hacks.mozilla.org/2015/03/understanding-inline-box-model/
- https://academind.com/learn/html/beginner-s-guide/diving-deeper-into-html/#block-level-vs-inline-elements
- https://medium.com/collabcode/pare-de-chutar-e-aprenda-como-funciona-o-display-inline-block-4e6cba2f19d4

> Calculo de valores em propriedades `CSS` com `calc()`

É possível o calculo do tamanho das propriedades `CSS` utilizando o método `calc()`. Pode-se utilizar tamanhos porcentuais e realizar cálculos utilizando os operadores `+`, `-`, `*` e `/`. Exemplo:

```css
    .property {
        width: calc(100% - 100px);
    }
```

> Alinhamento vertical (`vertical-align`)

Alinhamento vertical pode ser utilizador com a propriedade `vertical-align`. Essa propriedade leva em consideração o elemento diretamente anterior e diretamente posterior ao aplicado. Para centralizar um conteúdo, pode-se fazer algo como:

```css
    div {
        vertical-align: middle;
    }
```

Mais em:
- https://css-tricks.com/almanac/properties/v/vertical-align/

> Pseudo classes e pseudo elemenents

As diferenças são:

- `pseudo class`: permite que se defina um estilo para um determinado estado de um elemento, como o estado `hover` ou `active`. É definido com `:` após a classe, seguido do nome do estado, como em `.classe:hover`;

- `pseudo element`: permite que se defina um estilo para uma determinada porção de um elemento. É definido com `::` após o elemento, seguidos da porção específica, como em `p::first-line` ou `p::first-letter`. Pode-se usar algo como `.menu-items::after { content: " (Link)" }` para acrescentar o texto `(Link)` a frente de um item de menu, ou mesmo outros atributos que permitam a inserção de imagens.

Mais em:
- https://www.w3schools.com/css/css_pseudo_classes.asp
- https://developer.mozilla.org/pt-BR/docs/Web/CSS/Pseudo-elementos

> Inserir imagens no background

Para inserir imagens no background, basta usar a propriedade `background` com a função helper `url()` tal como em `.classe { background: url("freedom.jpg") }`.

> Relembrando - estrutura e propriedades mais usadas

A estrutura do `CSS` é composta por:

```css
seletor { 
    propriedade: valor;
}
```

As propriedades mais usadas são:

- color
- background-color
- display
- padding
- border
- margin
- width
- height

> display: none x visibility: hidden

Há uma diferença entre `display: none` e entre `visibility: hidden`: enquanto o primeiro retira o elemento da visualização, inclusive liberando seu espaço, o segundo apenas "esconde" o elemento, o tornando invisível enquanto seu espaço permanece preenchido. De qualquer forma, o elemento sempre permanece disponível no `DOM`.

## Seção 4

> Ordem de definição de estilos

Caso tenham 2 estilos em um mesmo elemento que estejam mudando a mesma característica deste elemento, como por exemplo a cor, o último estilo definido irá sobrepor o anterior.

> classes x IDs

`Classes` e `IDs` tem usos distintos:

- `Classes`:
    - São reusáveis;
    - Usadas somente com o propósito de estilizar;
    - Muito usadas como `seletores`.

- `IDs`:
    - Apenas um `ID` único por página;
    - Possui usos que vão além da estilização, como identificação na página para processamento de `javascript`;
    - Usados como seletores geralmente em último caso.

> O uso do `!important`

Podemos usar a anotação `!important` para impedir que a definição de uma propriedade seja sobrescrita, ou justamente para sobreescrever outra propriedade com determinado estilo. Em outras palavras, mesmo que uma propriedade tente sobrescrevê-la, uma propriedade com `!important` não será sobrescrita - a menos que a próxima propriedade também tenha a notação `!important`. No geral, não é uma boa prática usá-la por frequentemente levar a estilos confusos. Exemplo de uso: `div { color: blue !important }`;

> O uso de `:not()`

Essa pseudo classe permite a estilizar um elemento a partir da negação de um estado. Assim sendo, podemos usar `a:not(.active) { color: blue }`, por exemplo, para estilizar com a cor azul todo link que não estiver ativo. Deve-se usá-la com cuidado, por seu processamento não é tão eficaz quanto pseudo classes "diretas".

> Como verificar o suporte dos features nos browsers disponíveis

Podemos validar o suporte de cada feature nos browsers disponíveis por meio da página `MDN do feature` ou mesmo do site `caniuse.com`. 

## Seção 5

> A propriedade box-shadow

A propriedade box-shadow permite criar uma sombra atrás de um elemento qualquer. Você pode especificar mais de um efeito, os separando com virgulas. A sombra é constituída dos seguintes valores:

- `inset`: caso seja declarado, fará com que a sombra fique dentro da moldura. Nesse caso, a sombra ficará atrás do conteúdo, mas dentro da borda;
- `offset-x` e `offset-y`: são os desvios verticais e horizontais da sombra;
- `blur-radius`: ativa um efeito de desfocagem na sombra. Quanto maior o valor, maior o efeito;
- `spread-radius`: faz com que a sombra expanda e cresça;
- `color`: define uma cor para a sombra.

Exemplo: 
```css
.el {
    box-shadow: 4px 4px 1px 0px rgba(0, 0, 0, 0.5);
}
```

Mais em:
- https://developer.mozilla.org/pt-BR/docs/Web/CSS/box-shadow

> Método `rgba()`

O método `rgba()` permite a definição de uma cor por meio de `3` números, cada um definido entre `0` e `255` para as cores `Red`, `Green` e `Blue`, mais um número entre `0` e `1` para definição da transparência da cor.

Exemplo: 
```css
.el {
    background: rgba(0, 0, 0, 0.5);
}
```

> A propriedade `border-radius`

Caso quisermos utilizar cantos arredondados em nossos elementos, podemos utilizar a propriedade `border-radius`. Devemos utilizar com 4 valores, os quais serão utilizados para definir o tamanho do raio de cada canto do elemento, ou apenas um valor para todos os cantos. Exemplo: `.el { border-radius: 3px }`.

> Mudar cursor em um determinado elemento (propriedade `cursor`)

Para mudar o cursor quando em cima de um botão, podemos usar a propriedade `cursor` dessa forma: `.el { cursor: pointer }`.

> Retirar a borda de `focus` com `outline`

Quando o botão está no estado `focus`, um estilo é aplicado como uma fina borda. Para retirar esse estilo, pode ser usado o atributo `outline`, como em `.el:focus { outline: none; }`.

> As propriedades `float`, `clear` e `overflow`

A propriedade `float` cria um novo **contexto** para o visualização do elemento, mostrando ele a frente do elemento posterior.

Isso significa que em:

```html
    <div class="cards">
        <div class="card" id="div1"></div>
        <div class="card" id="div2"></div>
        <div class="card" id="div3"></div>
        <p>some text</p>
    </div>
```

```css
    .cards {
        background: red;
    }

    .card {
        height: 200px;
        width: 400px;
    }

    #div2 {
        float: right;
    }
```

O elemento `div2` será posicionado à frente do elemento `div3`, pois possui o atributo `float`.

Para que `div3` não fique atrás do elemento `div2`, podemos usar a propriedade `clear`, informando qual o lado que ele deverá desconsiderar o `float`:

```css
    #div3 {
        clear: right;
    }
```

Na verdade, ele "cria" um novo contexto, levando em consideração todos os níveis de contexto anteriores, e posicionando `div3` logo abaixo. Pode-se usar `#div { clear: both }` para levar em consideração ambos os lados de `float`.

Ainda há mais um ponto: caso todos os elementos com a classe `card` estiverem com a propriedade `float`, a cor de `background` ocupará apenas o espaço de `p`, pois nesse caso, será o único elemento no mesmo contexto de `cards`. Para corrigir isso, e recalcular a área levando em consideração todos os contextos criados, podemos usar o elemento `overflow`:

```css
    .cards {
        background: red;
        overflow: hidden;
    }
```

Mais em:
- https://medium.com/collabcode/pare-de-chutar-e-aprenda-como-funciona-o-float-left-e-float-right-e-sua-trupe-a4f4161114c7;
- https://www.w3schools.com/css/css_float.asp;

