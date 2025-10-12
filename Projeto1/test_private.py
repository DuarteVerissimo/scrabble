import pytest 
import sys
import FP2526P1 as fp  # <--- Change the name FP2526P1 to the file name with your project

class TestCriaConjunto:
    def test_1(self):
        saco = {'A': 1, 'B':3, 'Z':2, 'Ç':4}
        assert fp.cria_conjunto(('A','Z', 'B', 'Ç'), (1, 2, 3, 4)) == saco
    def test_2(self):
        saco = {}
        assert fp.cria_conjunto((), ()) == saco
    def test_3(self):
        saco = {'A': 1}
        assert fp.cria_conjunto(('A',), (1,)) == saco
    def test_4(self):
        saco = {'A': 1, 'B':1, 'C':1, 'Ç':1, 'D':1, 'E':1, 'F':1, 'G':1, 'H':1, 'I':1, 'J':1, 'L':1, 'M':1,
                'N':1, 'O':1, 'P':1, 'Q':1, 'R':1, 'S':1, 'T':1, 'U':1, 'V':1, 'X':1, 'Z':1}
        letras = ('A','B','C', 'Ç', 'D','E','F','G','H','I','J','L','M',
                  'N','O','P','Q','R','S','T','U','V','X','Z')
        contagem = (1,)*24
        assert fp.cria_conjunto(letras, contagem) == saco
        
class TestCriaConjuntoExceptions:
    def test_1(self):
        with pytest.raises(ValueError) as excinfo:
            fp.cria_conjunto(('A','B'), (14, 3, 1))
        assert 'cria_conjunto: argumentos inválidos' == str(excinfo.value)
        
    def test_2(self):
        with pytest.raises(ValueError) as excinfo:
            fp.cria_conjunto(('A','B', 'A'), (14, 3, 1))
        assert 'cria_conjunto: argumentos inválidos' == str(excinfo.value)
    def test_3(self):
        with pytest.raises(ValueError) as excinfo:
            fp.cria_conjunto(('A','B', '1'), (14, 3, 1))
        assert 'cria_conjunto: argumentos inválidos' == str(excinfo.value)
    def test_4(self):
        with pytest.raises(ValueError) as excinfo:
            fp.cria_conjunto(('A','B', 'C'), (14, 0, 1))
        assert 'cria_conjunto: argumentos inválidos' == str(excinfo.value)
    
    def test_5(self):
        with pytest.raises(ValueError) as excinfo:
            fp.cria_conjunto(4, (14, 0, 1))
        assert 'cria_conjunto: argumentos inválidos' == str(excinfo.value)
    
    def test_6(self):
        with pytest.raises(ValueError) as excinfo:
            fp.cria_conjunto(('A','B', 'C'), True)
        assert 'cria_conjunto: argumentos inválidos' == str(excinfo.value)
    
    def test_7(self):
        with pytest.raises(ValueError) as excinfo:
            fp.cria_conjunto(['A','B', 'C'], (14, 4, 1))
        assert 'cria_conjunto: argumentos inválidos' == str(excinfo.value)
    
    def test_8(self):
        with pytest.raises(ValueError) as excinfo:
            fp.cria_conjunto(('A','B', 'C'), (14, 4))
        assert 'cria_conjunto: argumentos inválidos' == str(excinfo.value)
    
    def test_9(self):
        with pytest.raises(ValueError) as excinfo:
            fp.cria_conjunto(('A','B', 'K'), (14, 4, 2))
        assert 'cria_conjunto: argumentos inválidos' == str(excinfo.value)
    
    def test_10(self):
        with pytest.raises(ValueError) as excinfo:
            fp.cria_conjunto(('A','Y', 'W'), (14, 4, 2))
        assert 'cria_conjunto: argumentos inválidos' == str(excinfo.value)
    
class TestGeraNumeroAleatorio:
    def test_1(self):
        assert fp.gera_numero_aleatorio(123456) == 3044438244
        
    def test_2(self):
        assert fp.gera_numero_aleatorio(444444) == 4188125022
        
    def test_3(self):
        t = (270369, 540738, 811107, 1081476, 1351845, 1622214, 1892583, 2162952, 2433321, 2703690)
        assert tuple(fp.gera_numero_aleatorio(n) for n in range(1,11)) == t
       
    def test_4(self):
        lst = [1]
        ref = [1, 270369, 67634689, 2647435461, 307599695, 2398689233, 745495504, 632435482, 435756210, 2005365029, 2916098932]
        for _ in range(10): lst.append(fp.gera_numero_aleatorio(lst[-1]))
        assert lst == ref

class TestPermutaLetras:
    def test_1(self):
        letras = list('ABCÇDEFGHIJLMNOPQRSTUVXZ') 
        assert fp.permuta_letras(letras, 123456) is None and \
            letras == ['F', 'I', 'G', 'E', 'P', 'X', 'Z', 'B', 'U', 'D', 'V', 'T', 'C', 'H', 'N', 'A', 'R', 'S', 'J', 'O', 'Q', 'L', 'Ç', 'M']
    
    def test_2(self):
        letras = list('ABCÇDEFGHIJLMNOPQRSTUVXZ') 
        assert fp.permuta_letras(letras, 444444) is None and \
            letras == ['P', 'M', 'S', 'N', 'H', 'C', 'O', 'A', 'L', 'Q', 'I', 'D', 'T', 'Z', 'X', 'B', 'V', 'R', 'G', 'E', 'Ç', 'U', 'J', 'F']
    
    def test_3(self):
        letras = list('ABCÇDEFGHIJLMNOPQRSTUVXZ')
        fp.permuta_letras(letras, 1)
        fp.permuta_letras(letras, 2) 
        assert letras == ['D', 'S', 'R', 'B', 'C', 'X', 'Q', 'E', 'U', 'O', 'L', 'Ç', 'P', 'I', 'H', 'A', 'T', 'V', 'N', 'G', 'M', 'F', 'J', 'Z']
    
    def test_4(self):
        letras = list('ABCÇDEFGHIJLMNOPQRSTUVXZ')[::2]
        for n in range(10): fp.permuta_letras(letras, 55) 
        assert letras == ['C', 'O', 'H', 'M', 'D', 'F', 'S', 'J', 'X', 'A', 'U', 'Q']
    
    def test_5(self):
        letras = []
        assert fp.permuta_letras(letras, 444444) is None and \
            not letras
    
    def test_6(self):
        letras = ['A']
        assert fp.permuta_letras(letras, 444444) is None and \
            letras == ['A']
        
class TestBaralhaConjunto:
    def test_1(self):
        letras = tuple('ABCÇDEFGHIJLMNOPQRSTUVXZ')[::3]
        saco = fp.cria_conjunto(letras, tuple(range(1, len(letras)+1)))
        saco2 = saco.copy()
        assert fp.baralha_conjunto(saco, 55) == \
                ['V', 'S', 'M', 'P', 'S', 'A', 'I', 'S', 'F', 'Ç', 
                 'M', 'V', 'S', 'P', 'P', 'M', 'F', 'Ç', 'S', 'V', 
                 'F', 'I', 'P', 'V', 'V', 'S', 'S', 'M', 'V', 'I', 
                 'M', 'V', 'I', 'V', 'P', 'P'] and \
                     saco == saco2
                
    def test_2(self):
        saco = fp.cria_conjunto(('E','B','N','L'), (4,2,3,3))
        assert fp.baralha_conjunto(saco, 324) == \
            ['N', 'E', 'N', 'E', 'B', 'L', 'E', 'N', 'L', 'L', 
             'E', 'B'] and saco == fp.cria_conjunto(('E','B','N','L'), (4,2,3,3)) 
        
    def test_3(self):
        saco = fp.cria_conjunto(('A','B','C','D'), (4,2,3,3))
        assert fp.baralha_conjunto(saco, 444444) == \
        ['A', 'D', 'D', 'A', 'C', 'C', 'B', 'B', 'A', 'D', 'A', 'C'] and \
            saco == fp.cria_conjunto(('A','B','C','D'), (4,2,3,3))

    def test_4(self):
        saco = fp.cria_conjunto((), ())
        assert fp.baralha_conjunto(saco, 444444) == []
    
    def test_5(self):
        saco = fp.cria_conjunto(('A',), (1,))
        assert fp.baralha_conjunto(saco, 34) == ['A']
    
    def test_6(self):
        saco = {
        'A': 14, 'B': 3, 'C': 4, 'Ç': 2, 'D': 5, 'E': 11, 'F': 2, 'G': 2, 'H': 2,
        'I': 10, 'J': 2, 'L': 5, 'M': 6, 'N': 4, 'O': 10, 'P': 4, 'Q': 1,
        'R': 6, 'S': 8, 'T': 5, 'U': 7, 'V': 2, 'X': 1, 'Z': 1 }
        
        saco2 = saco.copy()
        assert fp.baralha_conjunto(saco, 34) == \
            ['I', 'R', 'T', 'M', 'A', 'F', 'O', 'U', 'A', 'R', 
             'E', 'I', 'D', 'O', 'N', 'U', 'A', 'E', 'I', 'I', 
             'C', 'U', 'E', 'L', 'E', 'Z', 'O', 'O', 'O', 'T', 
             'C', 'S', 'L', 'B', 'A', 'V', 'A', 'H', 'C', 'C', 
             'I', 'S', 'P', 'N', 'E', 'B', 'E', 'A', 'P', 'S', 
             'J', 'U', 'S', 'T', 'M', 'B', 'Q', 'M', 'F', 'A', 
             'L', 'E', 'S', 'Ç', 'M', 'V', 'E', 'T', 'D', 'I', 
             'G', 'U', 'D', 'A', 'R', 'A', 'S', 'I', 'E', 'A', 
             'R', 'M', 'U', 'A', 'T', 'N', 'O', 'R', 'I', 'G', 
             'L', 'E', 'O', 'J', 'Ç', 'A', 'R', 'S', 'I', 'A', 
             'H', 'A', 'O', 'P', 'D', 'S', 'X', 'M', 'P', 'I', 
             'O', 'U', 'O', 'E', 'L', 'N', 'D'] and saco == saco2
      

class TestTestaPalavraPadrao:
    def test_1(self):
        conjunto = fp.cria_conjunto(('A','C','S','V'), (1,2,1,1))
        conjunto2 = conjunto.copy()
        assert not fp.testa_palavra_padrao('VACA', 'VA..S', conjunto) and conjunto == conjunto2
        
    def test_2(self):
        conjunto = fp.cria_conjunto(('A','C','S','V'), (2,2,1,1))
        conjunto2 = conjunto.copy()
        assert not fp.testa_palavra_padrao('VACA', '.E..', conjunto) and conjunto == conjunto2
        
    def test_3(self):
        conjunto = fp.cria_conjunto(('A','C','S','V'), (1,2,1,1))
        conjunto2 = conjunto.copy()
        assert not fp.testa_palavra_padrao('VACA', '.AL.', conjunto) and conjunto == conjunto2
        
    def test_4(self):
        conjunto = fp.cria_conjunto(('A','E','I','O', 'U'), (1,1,1,1, 1))
        conjunto2 = conjunto.copy()
        assert fp.testa_palavra_padrao('MAMEMIMOMU', 'M.M.M.M.M.', conjunto) and conjunto == conjunto2
    
    def test_5(self):
        conjunto = fp.cria_conjunto(('A','E','I', 'U'), (1,1,1,1))
        conjunto2 = conjunto.copy()
        assert not fp.testa_palavra_padrao('MANEPIROSU', 'M.N.P.R.S.', conjunto) and conjunto == conjunto2
          
    def test_6(self):
        conjunto = fp.cria_conjunto(('A','E','I', 'U', 'M'), (1,1,1,1, 4))
        conjunto2 = conjunto.copy()
        assert not fp.testa_palavra_padrao('MAMEMIMOMU', '.A.E.I.O.U', conjunto) and conjunto == conjunto2
          
    def test_7(self):
        conjunto = fp.cria_conjunto(('A','E','I', 'U', 'M'), (1,1,1,1, 5))
        conjunto2 = conjunto.copy()
        assert fp.testa_palavra_padrao('MAMEMIMOMU', '.A.E.I.O.U', conjunto) and conjunto == conjunto2
          
    def test_8(self):
        conjunto = fp.cria_conjunto(('Ç','E','I', 'U', 'M'), (1,1,1,1, 5))
        conjunto2 = conjunto.copy()
        assert fp.testa_palavra_padrao('CAÇA', 'CA.A', conjunto) and conjunto == conjunto2
          
    def test_9(self):
        conjunto = fp.cria_conjunto(('C','A','M', 'L', 'E'), (1,4,1,1, 5))
        conjunto2 = conjunto.copy()
        assert not fp.testa_palavra_padrao('CAMALEAO', '........', conjunto) and conjunto == conjunto2
          
    def test_10(self):
        conjunto = fp.cria_conjunto(('C','A','M', 'L', 'E', 'O'), (1,4,1,1, 5, 3))
        conjunto2 = conjunto.copy()
        assert fp.testa_palavra_padrao('CAMALEAO', '........', conjunto) and conjunto == conjunto2

          
class TestCriaTabuleiro:
    def test_1(self):
        tab =  [['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.']]
        assert fp.cria_tabuleiro() == tab

class TestCriaCasa:
    def test_1(self):
        with pytest.raises(ValueError) as excinfo:
            fp.cria_casa(200, 10)
        assert "cria_casa: argumentos inválidos" == str(excinfo.value)
        
    def test_2(self):
        with pytest.raises(ValueError) as excinfo:
            fp.cria_casa(10, (10,))
        assert "cria_casa: argumentos inválidos" == str(excinfo.value)
     
    def test_3(self):
        with pytest.raises(ValueError) as excinfo:
            fp.cria_casa(10, 200)
        assert "cria_casa: argumentos inválidos" == str(excinfo.value)
     
    def test_4(self):
        with pytest.raises(ValueError) as excinfo:
            fp.cria_casa('1', 7)
        assert "cria_casa: argumentos inválidos" == str(excinfo.value)
    
    def test_5(self):
        with pytest.raises(ValueError) as excinfo:
            fp.cria_casa(10, -7)
        assert "cria_casa: argumentos inválidos" == str(excinfo.value)
      
    def test_6(self):
        with pytest.raises(ValueError) as excinfo:
            fp.cria_casa(10.0, 8)
        assert "cria_casa: argumentos inválidos" == str(excinfo.value)
      
    def test_7(self):
        with pytest.raises(ValueError) as excinfo:
            fp.cria_casa(0, 8)
        assert "cria_casa: argumentos inválidos" == str(excinfo.value)
    
    def test_8(self):
        assert fp.cria_casa(15,15) == (15,15)

    def test_9(self):
        assert fp.cria_casa(4,5) == (4,5) and fp.cria_casa(5,4) == (5,4)

    def test_10(self):
        assert fp.cria_casa(15,1) == (15,1) and fp.cria_casa(1,15) == (1,15)

class TestObtemValor:
    def test_1(self):
        tab = \
           [['C', 'P', 'H', 'T', 'I', 'J', 'E', 'A', 'M', 'U', 'X', 'R', 'G', 'S', 'N'],
            ['E', 'J', 'F', 'I', 'B', 'O', 'P', 'U', 'H', 'C', 'R', 'G', 'N', 'S', 'T'],
            ['X', 'S', 'B', 'Z', 'V', 'P', 'D', 'H', 'R', 'O', 'Q', 'N', 'G', 'F', 'C'],
            ['N', 'I', 'A', 'V', 'T', 'S', 'Z', 'R', 'O', 'Ç', 'M', 'X', 'B', 'P', 'D'],
            ['T', 'F', 'G', 'N', 'L', 'Ç', 'A', 'J', 'H', 'S', 'Q', 'U', 'V', 'B', 'X'],
            ['U', 'Q', 'T', 'A', 'O', 'R', 'H', 'I', 'D', 'X', 'E', 'Ç', 'N', 'F', 'L'],
            ['L', 'D', 'I', 'B', 'A', 'U', 'Z', 'M', 'P', 'C', 'X', 'R', 'V', 'Ç', 'N'],
            ['U', 'P', 'V', 'E', 'Z', 'O', 'C', 'Ç', 'B', 'R', 'M', 'I', 'X', 'H', 'L'],
            ['A', 'L', 'F', 'I', 'Q', 'C', 'T', 'R', 'Ç', 'Z', 'E', 'M', 'O', 'N', 'V'],
            ['G', 'I', 'M', 'B', 'T', 'Q', 'P', 'E', 'V', 'F', 'R', 'L', 'Ç', 'H', 'A'],
            ['X', 'C', 'T', 'V', 'N', 'L', 'R', 'G', 'P', 'O', 'H', 'J', 'B', 'A', 'M'],
            ['H', 'F', 'O', 'T', 'Q', 'L', 'J', 'I', 'D', 'S', 'Ç', 'B', 'C', 'E', 'X'],
            ['O', 'G', 'D', 'V', 'X', 'C', 'H', 'L', 'I', 'F', 'U', 'Z', 'S', 'R', 'J'],
            ['Z', 'E', 'Ç', 'I', 'G', 'M', 'A', 'H', 'F', 'L', 'D', 'P', 'J', 'T', 'X'],
            ['O', 'T', 'V', 'X', 'B', 'Ç', 'E', 'U', 'N', 'A', 'J', 'I', 'Q', 'G', 'S']]
        
        assert tuple(fp.obtem_valor(tab, (i,i-1)) for i in range(2,15,2)) == ('E', 'A', 'O', 'C', 'V', 'Ç', 'J')
        
    def test_2(self):
        tab = \
           [['C', 'P', 'H', 'T', 'I', 'J', 'E', 'A', 'M', 'U', 'X', 'R', 'G', 'S', 'N'],
            ['E', 'J', 'F', 'I', 'B', 'O', 'P', 'U', 'H', 'C', 'R', 'G', 'N', 'S', 'T'],
            ['X', 'S', 'B', 'Z', 'V', 'P', 'D', 'H', 'R', 'O', 'Q', 'N', 'G', 'F', 'C'],
            ['N', 'I', 'A', 'V', 'T', 'S', 'Z', 'R', 'O', 'Ç', 'M', 'X', 'B', 'P', 'D'],
            ['T', 'F', 'G', 'N', 'L', 'Ç', 'A', 'J', 'H', 'S', 'Q', 'U', 'V', 'B', 'X'],
            ['U', 'Q', 'T', 'A', 'O', 'R', 'H', 'I', 'D', 'X', 'E', 'Ç', 'N', 'F', 'L'],
            ['L', 'D', 'I', 'B', 'A', 'U', 'Z', 'M', 'P', 'C', 'X', 'R', 'V', 'Ç', 'N'],
            ['U', 'P', 'V', 'E', 'Z', 'O', 'C', 'Ç', 'B', 'R', 'M', 'I', 'X', 'H', 'L'],
            ['A', 'L', 'F', 'I', 'Q', 'C', 'T', 'R', 'Ç', 'Z', 'E', 'M', 'O', 'N', 'V'],
            ['G', 'I', 'M', 'B', 'T', 'Q', 'P', 'E', 'V', 'F', 'R', 'L', 'Ç', 'H', 'A'],
            ['X', 'C', 'T', 'V', 'N', 'L', 'R', 'G', 'P', 'O', 'H', 'J', 'B', 'A', 'M'],
            ['H', 'F', 'O', 'T', 'Q', 'L', 'J', 'I', 'D', 'S', 'Ç', 'B', 'C', 'E', 'X'],
            ['O', 'G', 'D', 'V', 'X', 'C', 'H', 'L', 'I', 'F', 'U', 'Z', 'S', 'R', 'J'],
            ['Z', 'E', 'Ç', 'I', 'G', 'M', 'A', 'H', 'F', 'L', 'D', 'P', 'J', 'T', 'X'],
            ['O', 'T', 'V', 'X', 'B', 'Ç', 'E', 'U', 'N', 'A', 'J', 'I', 'Q', 'G', 'S']]
        
        assert tuple(fp.obtem_valor(tab, (i,i+1)) for i in range(1,14,2)) == ('P', 'Z', 'Ç', 'M', 'Z', 'J', 'R')
        
class TestInsereLetra:
    def test_1(self):
        tab = fp.cria_tabuleiro()
        tab2 = fp.insere_letra(tab, (1,5), 'A')
        
        assert tab == tab2 and id(tab) == id(tab2)
        
    def test_2(self):
        tab = fp.cria_tabuleiro()
        fp.insere_letra(tab, (1,5), 'A')
        
        assert tab[0][4] == 'A' and all(tab[i][j] == '.' for i in range(15) for j in range(15) if (i,j) != (0,4))
        
        
    def test_3(self):
        tab = fp.cria_tabuleiro()
        letras = ['B', 'I', 'V', 'F', 'J', 'L', 'H', 'S', 'P', 'D', 
                  'X', 'Ç', 'T', 'O', 'E', 'R', 'M', 'U', 'G', 'Z', 
                  'Q', 'N', 'A', 'C']
        for i in range(1,14): fp.insere_letra(tab, (i,i+1), letras.pop()) 
        
        assert tab == \
            [['.', 'C', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', 'A', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', 'N', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', 'Q', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', 'Z', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', 'G', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', 'U', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', 'M', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', 'R', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'E', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'O', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'T', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'Ç', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.']]
    
    def test_4(self):
        tab = fp.cria_tabuleiro()
        letras = ['O', 'L', 'C', 'A', 'N', 'V', 'D', 'Z', 'M', 'S', 'F', 'Q', 'U', 'H', 'T', 'B', 'X', 'G', 'E', 'J', 'P', 'Ç', 'I', 'R']
        for i in range(2,15): fp.insere_letra(tab, (i,16-i), letras.pop())
        assert tab == \
            [['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
 ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'R', '.'],
 ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'I', '.', '.'],
 ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'Ç', '.', '.', '.'],
 ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'P', '.', '.', '.', '.'],
 ['.', '.', '.', '.', '.', '.', '.', '.', '.', 'J', '.', '.', '.', '.', '.'],
 ['.', '.', '.', '.', '.', '.', '.', '.', 'E', '.', '.', '.', '.', '.', '.'],
 ['.', '.', '.', '.', '.', '.', '.', 'G', '.', '.', '.', '.', '.', '.', '.'],
 ['.', '.', '.', '.', '.', '.', 'X', '.', '.', '.', '.', '.', '.', '.', '.'],
 ['.', '.', '.', '.', '.', 'B', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
 ['.', '.', '.', '.', 'T', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
 ['.', '.', '.', 'H', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
 ['.', '.', 'U', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
 ['.', 'Q', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
 ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.']]

class TestObtemSequencia:
    def test_1(self):
        tab = [['C', 'P', 'H', 'T', 'I', '.', '.', '.', '.', 'U', 'X', '.', 'G', '.', 'N'],
 ['E', '.', '.', 'I', 'B', 'O', 'P', '.', 'H', 'C', 'R', '.', 'N', 'S', 'T'],
 ['X', 'S', 'B', '.', 'V', 'P', 'D', 'H', 'R', 'O', 'Q', 'N', '.', 'F', 'C'],
 ['.', 'I', 'A', 'V', '.', '.', 'Z', 'R', 'O', 'Ç', 'M', '.', 'B', 'P', 'D'],
 ['T', 'F', 'G', 'N', 'L', 'Ç', '.', 'J', 'H', '.', '.', 'U', '.', 'B', '.'],
 ['.', 'Q', 'T', 'A', 'O', 'R', 'H', '.', 'D', '.', 'E', 'Ç', '.', '.', '.'],
 ['L', '.', '.', 'B', 'A', '.', '.', '.', '.', 'C', 'X', '.', 'V', '.', '.'],
 ['U', 'P', '.', '.', 'Z', '.', 'C', 'Ç', '.', 'R', 'M', 'I', '.', '.', '.'],
 ['A', '.', 'F', 'I', 'Q', 'C', '.', 'R', '.', '.', '.', '.', '.', 'N', '.'],
 ['G', 'I', 'M', 'B', 'T', 'Q', '.', '.', 'V', 'F', 'R', '.', 'Ç', 'H', '.'],
 ['X', 'C', '.', '.', '.', '.', '.', '.', 'P', 'O', '.', '.', 'B', 'A', 'M'],
 ['H', '.', '.', 'T', 'Q', 'L', '.', 'I', 'D', 'S', 'Ç', 'B', '.', 'E', 'X'],
 ['O', 'G', '.', '.', 'X', 'C', 'H', '.', 'I', 'F', 'U', '.', 'S', 'R', 'J'],
 ['.', 'E', 'Ç', '.', 'G', 'M', '.', '.', '.', 'L', 'D', 'P', '.', 'T', 'X'],
 ['O', 'T', 'V', 'X', '.', '.', 'E', 'U', 'N', 'A', '.', 'I', '.', 'G', 'S']]
        assert fp.obtem_sequencia(tab, (8,7), 'V', 8) == 'C....H.E'
      
    def test_2(self):
        tab = [['C', 'P', 'H', 'T', 'I', '.', '.', '.', '.', 'U', 'X', '.', 'G', '.', 'N'],
 ['E', '.', '.', 'I', 'B', 'O', 'P', '.', 'H', 'C', 'R', '.', 'N', 'S', 'T'],
 ['X', 'S', 'B', '.', 'V', 'P', 'D', 'H', 'R', 'O', 'Q', 'N', '.', 'F', 'C'],
 ['.', 'I', 'A', 'V', '.', '.', 'Z', 'R', 'O', 'Ç', 'M', '.', 'B', 'P', 'D'],
 ['T', 'F', 'G', 'N', 'L', 'Ç', '.', 'J', 'H', '.', '.', 'U', '.', 'B', '.'],
 ['.', 'Q', 'T', 'A', 'O', 'R', 'H', '.', 'D', '.', 'E', 'Ç', '.', '.', '.'],
 ['L', '.', '.', 'B', 'A', '.', '.', '.', '.', 'C', 'X', '.', 'V', '.', '.'],
 ['U', 'P', '.', '.', 'Z', '.', 'C', 'Ç', '.', 'R', 'M', 'I', '.', '.', '.'],
 ['A', '.', 'F', 'I', 'Q', 'C', '.', 'R', '.', '.', '.', '.', '.', 'N', '.'],
 ['G', 'I', 'M', 'B', 'T', 'Q', '.', '.', 'V', 'F', 'R', '.', 'Ç', 'H', '.'],
 ['X', 'C', '.', '.', '.', '.', '.', '.', 'P', 'O', '.', '.', 'B', 'A', 'M'],
 ['H', '.', '.', 'T', 'Q', 'L', '.', 'I', 'D', 'S', 'Ç', 'B', '.', 'E', 'X'],
 ['O', 'G', '.', '.', 'X', 'C', 'H', '.', 'I', 'F', 'U', '.', 'S', 'R', 'J'],
 ['.', 'E', 'Ç', '.', 'G', 'M', '.', '.', '.', 'L', 'D', 'P', '.', 'T', 'X'],
 ['O', 'T', 'V', 'X', '.', '.', 'E', 'U', 'N', 'A', '.', 'I', '.', 'G', 'S']]
        assert fp.obtem_sequencia(tab, (8,4), 'H', 5) == '.Z.CÇ'   
          
    def test_3(self):
        tab = [['C', 'P', 'H', 'T', 'I', '.', '.', '.', '.', 'U', 'X', '.', 'G', '.', 'N'],
 ['E', '.', '.', 'I', 'B', 'O', 'P', '.', 'H', 'C', 'R', '.', 'N', 'S', 'T'],
 ['X', 'S', 'B', '.', 'V', 'P', 'D', 'H', 'R', 'O', 'Q', 'N', '.', 'F', 'C'],
 ['.', 'I', 'A', 'V', '.', '.', 'Z', 'R', 'O', 'Ç', 'M', '.', 'B', 'P', 'D'],
 ['T', 'F', 'G', 'N', 'L', 'Ç', '.', 'J', 'H', '.', '.', 'U', '.', 'B', '.'],
 ['.', 'Q', 'T', 'A', 'O', 'R', 'H', '.', 'D', '.', 'E', 'Ç', '.', '.', '.'],
 ['L', '.', '.', 'B', 'A', '.', '.', '.', '.', 'C', 'X', '.', 'V', '.', '.'],
 ['U', 'P', '.', '.', 'Z', '.', 'C', 'Ç', '.', 'R', 'M', 'I', '.', '.', '.'],
 ['A', '.', 'F', 'I', 'Q', 'C', '.', 'R', '.', '.', '.', '.', '.', 'N', '.'],
 ['G', 'I', 'M', 'B', 'T', 'Q', '.', '.', 'V', 'F', 'R', '.', 'Ç', 'H', '.'],
 ['X', 'C', '.', '.', '.', '.', '.', '.', 'P', 'O', '.', '.', 'B', 'A', 'M'],
 ['H', '.', '.', 'T', 'Q', 'L', '.', 'I', 'D', 'S', 'Ç', 'B', '.', 'E', 'X'],
 ['O', 'G', '.', '.', 'X', 'C', 'H', '.', 'I', 'F', 'U', '.', 'S', 'R', 'J'],
 ['.', 'E', 'Ç', '.', 'G', 'M', '.', '.', '.', 'L', 'D', 'P', '.', 'T', 'X'],
 ['O', 'T', 'V', 'X', '.', '.', 'E', 'U', 'N', 'A', '.', 'I', '.', 'G', 'S']]
        assert fp.obtem_sequencia(tab, (1,1), 'V', 15) == 'CEX.T.LUAGXHO.O'
               
    def test_4(self):
        tab = [['C', 'P', 'H', 'T', 'I', '.', '.', '.', '.', 'U', 'X', '.', 'G', '.', 'N'],
 ['E', '.', '.', 'I', 'B', 'O', 'P', '.', 'H', 'C', 'R', '.', 'N', 'S', 'T'],
 ['X', 'S', 'B', '.', 'V', 'P', 'D', 'H', 'R', 'O', 'Q', 'N', '.', 'F', 'C'],
 ['.', 'I', 'A', 'V', '.', '.', 'Z', 'R', 'O', 'Ç', 'M', '.', 'B', 'P', 'D'],
 ['T', 'F', 'G', 'N', 'L', 'Ç', '.', 'J', 'H', '.', '.', 'U', '.', 'B', '.'],
 ['.', 'Q', 'T', 'A', 'O', 'R', 'H', '.', 'D', '.', 'E', 'Ç', '.', '.', '.'],
 ['L', '.', '.', 'B', 'A', '.', '.', '.', '.', 'C', 'X', '.', 'V', '.', '.'],
 ['U', 'P', '.', '.', 'Z', '.', 'C', 'Ç', '.', 'R', 'M', 'I', '.', '.', '.'],
 ['A', '.', 'F', 'I', 'Q', 'C', '.', 'R', '.', '.', '.', '.', '.', 'N', '.'],
 ['G', 'I', 'M', 'B', 'T', 'Q', '.', '.', 'V', 'F', 'R', '.', 'Ç', 'H', '.'],
 ['X', 'C', '.', '.', '.', '.', '.', '.', 'P', 'O', '.', '.', 'B', 'A', 'M'],
 ['H', '.', '.', 'T', 'Q', 'L', '.', 'I', 'D', 'S', 'Ç', 'B', '.', 'E', 'X'],
 ['O', 'G', '.', '.', 'X', 'C', 'H', '.', 'I', 'F', 'U', '.', 'S', 'R', 'J'],
 ['.', 'E', 'Ç', '.', 'G', 'M', '.', '.', '.', 'L', 'D', 'P', '.', 'T', 'X'],
 ['O', 'T', 'V', 'X', '.', '.', 'E', 'U', 'N', 'A', '.', 'I', '.', 'G', 'S']]
        assert fp.obtem_sequencia(tab, (1,1), 'H', 15) == 'CPHTI....UX.G.N' 
    
class TestInserePalavra:
    def test_1(self):
        tab = fp.cria_tabuleiro()
        tab2 = fp.insere_palavra(tab, (1,5), 'PROGRAMA', 'H')
        
        assert tab == tab2 and id(tab) == id(tab2)
        
    def test_2(self):
        tab = fp.cria_tabuleiro()
        fp.insere_palavra(tab, (2,4), 'H', 'PROGRAMA')
        
        assert fp.obtem_sequencia(tab, (2,1), 'H', 15) == '...PROGRAMA....' and \
            fp.obtem_sequencia(tab, (2,4), 'H', len('PROGRAMA')) == 'PROGRAMA' and \
                all(tab[i][j] == '.' for i in range(15) for j in range(15) if i != 1)
    
    def test_3(self):
        tab = fp.cria_tabuleiro()
        fp.insere_palavra(tab, (5,7), 'V', 'PROGRAMA')
        
        assert fp.obtem_sequencia(tab, (1,7), 'V', 15) == '....PROGRAMA...' and \
            fp.obtem_sequencia(tab, (5,7), 'V', len('PROGRAMA')) == 'PROGRAMA' and \
                all(tab[i][j] == '.' for i in range(15) for j in range(15) if j != 6)
            
    def test_4(self):
        tab = fp.cria_tabuleiro()
        fp.insere_palavra(tab, (5,7), 'V', 'PROGRAMA')
        fp.insere_palavra(tab, (2,3), 'H', 'ALGORITMO')
        fp.insere_palavra(tab, (13,1), 'H', 'COMPUTADOR')
        fp.insere_palavra(tab, (12,12), 'V', 'TIPO')
        
        assert tab == \
            [['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
['.', '.', 'A', 'L', 'G', 'O', 'R', 'I', 'T', 'M', 'O', '.', '.', '.', '.'],
['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
['.', '.', '.', '.', '.', '.', 'P', '.', '.', '.', '.', '.', '.', '.', '.'],
['.', '.', '.', '.', '.', '.', 'R', '.', '.', '.', '.', '.', '.', '.', '.'],
['.', '.', '.', '.', '.', '.', 'O', '.', '.', '.', '.', '.', '.', '.', '.'],
['.', '.', '.', '.', '.', '.', 'G', '.', '.', '.', '.', '.', '.', '.', '.'],
['.', '.', '.', '.', '.', '.', 'R', '.', '.', '.', '.', '.', '.', '.', '.'],
['.', '.', '.', '.', '.', '.', 'A', '.', '.', '.', '.', '.', '.', '.', '.'],
['.', '.', '.', '.', '.', '.', 'M', '.', '.', '.', '.', '.', '.', '.', '.'],
['.', '.', '.', '.', '.', '.', 'A', '.', '.', '.', '.', 'T', '.', '.', '.'],
['C', 'O', 'M', 'P', 'U', 'T', 'A', 'D', 'O', 'R', '.', 'I', '.', '.', '.'],
['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'P', '.', '.', '.'],
['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'O', '.', '.', '.']]
        
class TestTabuleiroParaStr:
    def test_1(self):
        tab = \
            [['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', 'A', 'L', 'G', 'O', 'R', 'I', 'T', 'M', 'O', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', 'P', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', 'R', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', 'O', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', 'G', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', 'R', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', 'A', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', 'M', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', 'A', '.', '.', '.', '.', 'T', '.', '.', '.'],
            ['C', 'O', 'M', 'P', 'U', 'T', 'A', 'D', 'O', 'R', '.', 'I', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'P', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'O', '.', '.', '.']]
            
        assert fp.tabuleiro_para_str(tab) == \
"""                       1 1 1 1 1 1
     1 2 3 4 5 6 7 8 9 0 1 2 3 4 5
   +-------------------------------+
 1 | . . . . . . . . . . . . . . . |
 2 | . . A L G O R I T M O . . . . |
 3 | . . . . . . . . . . . . . . . |
 4 | . . . . . . . . . . . . . . . |
 5 | . . . . . . P . . . . . . . . |
 6 | . . . . . . R . . . . . . . . |
 7 | . . . . . . O . . . . . . . . |
 8 | . . . . . . G . . . . . . . . |
 9 | . . . . . . R . . . . . . . . |
10 | . . . . . . A . . . . . . . . |
11 | . . . . . . M . . . . . . . . |
12 | . . . . . . A . . . . T . . . |
13 | C O M P U T A D O R . I . . . |
14 | . . . . . . . . . . . P . . . |
15 | . . . . . . . . . . . O . . . |
   +-------------------------------+"""
   
    def test_2(self):
        tab = [['C', 'P', 'H', 'T', 'I', '.', '.', '.', '.', 'U', 'X', '.', 'G', '.', 'N'],
    ['E', '.', '.', 'I', 'B', 'O', 'P', '.', 'H', 'C', 'R', '.', 'N', 'S', 'T'],
    ['X', 'S', 'B', '.', 'V', 'P', 'D', 'H', 'R', 'O', 'Q', 'N', '.', 'F', 'C'],
    ['.', 'I', 'A', 'V', '.', '.', 'Z', 'R', 'O', 'Ç', 'M', '.', 'B', 'P', 'D'],
    ['T', 'F', 'G', 'N', 'L', 'Ç', '.', 'J', 'H', '.', '.', 'U', '.', 'B', '.'],
    ['.', 'Q', 'T', 'A', 'O', 'R', 'H', '.', 'D', '.', 'E', 'Ç', '.', '.', '.'],
    ['L', '.', '.', 'B', 'A', '.', '.', '.', '.', 'C', 'X', '.', 'V', '.', '.'],
    ['U', 'P', '.', '.', 'Z', '.', 'C', 'Ç', '.', 'R', 'M', 'I', '.', '.', '.'],
    ['A', '.', 'F', 'I', 'Q', 'C', '.', 'R', '.', '.', '.', '.', '.', 'N', '.'],
    ['G', 'I', 'M', 'B', 'T', 'Q', '.', '.', 'V', 'F', 'R', '.', 'Ç', 'H', '.'],
    ['X', 'C', '.', '.', '.', '.', '.', '.', 'P', 'O', '.', '.', 'B', 'A', 'M'],
    ['H', '.', '.', 'T', 'Q', 'L', '.', 'I', 'D', 'S', 'Ç', 'B', '.', 'E', 'X'],
    ['O', 'G', '.', '.', 'X', 'C', 'H', '.', 'I', 'F', 'U', '.', 'S', 'R', 'J'],
    ['.', 'E', 'Ç', '.', 'G', 'M', '.', '.', '.', 'L', 'D', 'P', '.', 'T', 'X'],
    ['O', 'T', 'V', 'X', '.', '.', 'E', 'U', 'N', 'A', '.', 'I', '.', 'G', 'S']]
        assert fp.tabuleiro_para_str(tab) == \
"""                       1 1 1 1 1 1
     1 2 3 4 5 6 7 8 9 0 1 2 3 4 5
   +-------------------------------+
 1 | C P H T I . . . . U X . G . N |
 2 | E . . I B O P . H C R . N S T |
 3 | X S B . V P D H R O Q N . F C |
 4 | . I A V . . Z R O Ç M . B P D |
 5 | T F G N L Ç . J H . . U . B . |
 6 | . Q T A O R H . D . E Ç . . . |
 7 | L . . B A . . . . C X . V . . |
 8 | U P . . Z . C Ç . R M I . . . |
 9 | A . F I Q C . R . . . . . N . |
10 | G I M B T Q . . V F R . Ç H . |
11 | X C . . . . . . P O . . B A M |
12 | H . . T Q L . I D S Ç B . E X |
13 | O G . . X C H . I F U . S R J |
14 | . E Ç . G M . . . L D P . T X |
15 | O T V X . . E U N A . I . G S |
   +-------------------------------+""" 
          
class TestCriaJogador:
    def test_1(self):
        assert fp.cria_jogador(1, 10, {'A':5}) == {'id':1, 'pontos':10, 'letras':{'A':5}}
    
    def test_2(self):
        with pytest.raises(ValueError) as excinfo:
            fp.cria_jogador(-11, 10, {'A':5})
        assert "cria_jogador: argumentos inválidos" == str(excinfo.value)
    
    def test_3(self):
        with pytest.raises(ValueError) as excinfo:
            fp.cria_jogador(2, -1, {})
        assert "cria_jogador: argumentos inválidos" == str(excinfo.value)
    
    def test_4(self):
        with pytest.raises(ValueError) as excinfo:
            fp.cria_jogador(3.0, 0, {})
        assert "cria_jogador: argumentos inválidos" == str(excinfo.value)
    
    def test_5(self):
        with pytest.raises(ValueError) as excinfo:
            fp.cria_jogador(3, 10.0, {})
        assert "cria_jogador: argumentos inválidos" == str(excinfo.value)
    
    def test_6(self):
        with pytest.raises(ValueError) as excinfo:
            fp.cria_jogador(3, 10, {'?':5})
        assert "cria_jogador: argumentos inválidos" == str(excinfo.value)
    
    def test_7(self):
        with pytest.raises(ValueError) as excinfo:
            fp.cria_jogador(3, 10, {5:'A'})
        assert "cria_jogador: argumentos inválidos" == str(excinfo.value)
    
    def test_8(self):
        with pytest.raises(ValueError) as excinfo:
            fp.cria_jogador(3, 10, {'A':3, 'B':2, 'C':-1})
        assert "cria_jogador: argumentos inválidos" == str(excinfo.value)
    
    def test_9(self):
        with pytest.raises(ValueError) as excinfo:
            fp.cria_jogador(3, 10, {'A':3, 'B':2, 'C':3})
        assert "cria_jogador: argumentos inválidos" == str(excinfo.value)
    
    
    def test_10(self):
        jogador = fp.cria_jogador(4, 5, {'A':3, 'B':1, 'C':3})
        assert jogador == {'id':4, 'pontos':5, 'letras':{'A':3, 'B':1, 'C':3}}     
        
class TestJogadorParaStr:
    def test_1(self):
        jogador = {'id':4, 'pontos':5, 'letras':{'C':3, 'B':1}}
        assert fp.jogador_para_str(jogador) == '#4 (  5): B C C C'
        
    def test_2(self):
        jogador = {'id':2, 'pontos':123, 'letras':{'Z':1, 'X':2, 'V':4}}
        assert fp.jogador_para_str(jogador) == '#2 (123): V V V V X X Z'
        
    def test_3(self):
        jogador = {'id':1, 'pontos':0, 'letras':{}}
        assert fp.jogador_para_str(jogador) == '#1 (  0): '
        
    def test_4(self):
        jogador = {'id':3, 'pontos':15, 'letras':{'Ç':2, 'A':1, 'D':3}}
        assert fp.jogador_para_str(jogador) == '#3 ( 15): A Ç Ç D D D'
      
class TestDistribuiLetras:
    def test_1(self):
        jog = {'id':1, 'pontos':0, 'letras':{'A':1, 'M':3}}
        
        letras = ['A', 'B', 'C', 'D']
        assert fp.distribui_letra(letras, jog) and letras == ['A', 'B', 'C'] and \
            jog == {'id':1, 'pontos':0, 'letras':{'A':1, 'M':3, 'D':1} } 
                                                                                                                        
    def test_2(self):
        jog = {'id':1, 'pontos':0, 'letras':{'A':1, 'M':3, 'D':1}}
        
        letras = ['A', 'B', 'C', 'D']
        assert fp.distribui_letra(letras, jog) and letras == ['A', 'B', 'C'] and \
            jog == {'id':1, 'pontos':0, 'letras':{'A':1, 'M':3, 'D':2} } 
                                                                                                                        
    def test_3(self):
        jog = {'id':3, 'pontos':1240, 'letras':{}}
        
        letras = ['M', 'O', 'N', 'O', 'P']
        res = tuple(fp.distribui_letra(letras, jog) for _ in range(6))
        assert  res == ((True,)*5 + (False,) ) and letras == [] and \
            jog == {'id':3, 'pontos':1240, 'letras':{'M':1, 'N':1, 'O':2, 'P':1} } 
                                  
    def test_4(self):
        jog = {'id':1, 'pontos':0, 'letras':{}}
        letras = []
        assert tuple(fp.distribui_letra(letras, jog) for _ in range(3)) == (False,)*3 and \
            jog == {'id':1, 'pontos':0, 'letras':{}}
        
class TestJogaPalavra:
    def test_1(self):
        tab = fp.cria_tabuleiro()
        conj = fp.cria_conjunto(('M', 'E', 'A', 'L'), (2,1,3,1))
        assert not fp.joga_palavra(tab, 'MEL', (7,7), 'V', conj, True) and \
            tab == fp.cria_tabuleiro() and \
            conj == fp.cria_conjunto(('M', 'E', 'A', 'L'), (2,1,3,1))
        
    def test_2(self):
        tab = fp.cria_tabuleiro()
        conj = fp.cria_conjunto(('M', 'E', 'A', 'L'), (2,1,3,1))
        assert fp.joga_palavra(tab, 'MEL', (7,8), 'V', conj, True) == ('E', 'L', 'M') and \
            fp.obtem_sequencia(tab, (7,8), 'V', len('MEL')) == 'MEL' and \
            conj == fp.cria_conjunto(('M', 'E', 'A', 'L'), (2,1,3,1))
        
    def test_3(self):
        tab = fp.cria_tabuleiro()
        conj = fp.cria_conjunto(('M', 'E', 'A', 'L'), (2,1,1,1))
        assert  fp.joga_palavra(tab, 'LAMA', (8,8), 'V', conj, True) == () and \
            tab == fp.cria_tabuleiro() and \
            conj == fp.cria_conjunto(('M', 'E', 'A', 'L'), (2,1,1,1))
            
    def test_4(self):
        tab = fp.cria_tabuleiro()
        conj_letras1 = fp.cria_conjunto(('C', 'A', 'O', 'N'),(2,1,3,1))
        #('C', 'C', 'A', 'O', 'O', 'O', 'N')
        assert fp.joga_palavra(tab, 'NOTA', fp.cria_casa(8,8), 'H', conj_letras1, True) == () and \
            conj_letras1 == fp.cria_conjunto(('C', 'A', 'O', 'N'),(2,1,3,1)) and \
            tab == fp.cria_tabuleiro()

    def test_5(self):
        tab = fp.cria_tabuleiro()
        conj_letras1 = fp.cria_conjunto(('C', 'A', 'O', 'N'),(2,1,3,1))
        assert fp.joga_palavra(tab, 'NAO', fp.cria_casa(7,8), 'H', conj_letras1, True) == () and \
            conj_letras1 == fp.cria_conjunto(('C', 'A', 'O', 'N'),(2,1,3,1)) and \
            tab == fp.cria_tabuleiro()
        
    def test_6(self):
        tab = fp.cria_tabuleiro()
        conj_letras1 = fp.cria_conjunto(('C', 'A', 'O', 'N'),(2,1,3,1))
        assert fp.joga_palavra(tab, 'NAO', fp.cria_casa(8,8), 'H', conj_letras1, False) == () and \
            conj_letras1 == fp.cria_conjunto(('C', 'A', 'O', 'N'),(2,1,3,1)) and \
            tab == fp.cria_tabuleiro()
            
    def test_7(self):
        tab = fp.cria_tabuleiro()
        conj_letras1 = fp.cria_conjunto(('C', 'A', 'O', 'N'),(2,1,3,1))
        assert fp.joga_palavra(tab, 'NAO', fp.cria_casa(8,8), 'H', conj_letras1, True) == ('A', 'N', 'O') and \
            fp.obtem_sequencia(tab, (8,8), 'H', len('NAO')) == 'NAO' and \
                conj_letras1 == fp.cria_conjunto(('C', 'A', 'O', 'N'),(2,1,3,1))    
   
    def test_8(self):
        tab = fp.cria_tabuleiro()
        conj_letras1 = fp.cria_conjunto(('C', 'A', 'O', 'N'),(2,1,3,1))
        conj_letras2 = fp.cria_conjunto(('O', 'I', 'S', 'R', 'A'),(2,1,2,1,1))
        fp.joga_palavra(tab, 'NAO', fp.cria_casa(8,8), 'H', conj_letras1, True)
        assert fp.joga_palavra(tab, 'RISO', fp.cria_casa(11,11), 'V', conj_letras2, False) == ()
       
    def test_9(self):
        tab = fp.cria_tabuleiro()
        conj_letras1 = fp.cria_conjunto(('C', 'A', 'O', 'N'),(2,1,3,1))
        conj_letras2 = fp.cria_conjunto(('O', 'I', 'S', 'R', 'A'),(2,1,2,1,1))
        fp.joga_palavra(tab, 'NAO', fp.cria_casa(8,8), 'H', conj_letras1, True)
        assert fp.joga_palavra(tab, 'RISO', fp.cria_casa(5,10), 'V', conj_letras2, False) == ('I', 'R', 'S')

    def test_10(self):
        tab = fp.cria_tabuleiro()
        conj_letras1 = fp.cria_conjunto(('C', 'A', 'O', 'N'),(2,1,3,1))
        conj_letras2 = fp.cria_conjunto(('O', 'I', 'S', 'R', 'A'),(2,1,2,1,1))
        fp.joga_palavra(tab, 'NAO', fp.cria_casa(8,8), 'H', conj_letras1, True)
        assert fp.joga_palavra(tab, 'AO', fp.cria_casa(8,9), 'V', conj_letras2, False) == ('O',)

    def test_11(self):
        tab = fp.cria_tabuleiro()
        conj_letras1 = fp.cria_conjunto(('C', 'A', 'O', 'N'),(2,1,3,1))
        conj_letras2 = fp.cria_conjunto(('O', 'I', 'S', 'R', 'A'),(2,1,2,1,1))
        fp.joga_palavra(tab, 'NAO', fp.cria_casa(8,8), 'H', conj_letras1, True)
        assert fp.joga_palavra(tab, 'AO', fp.cria_casa(8,9), 'H', conj_letras2, False) == ()
 
    def test_12(self):
        tab = \
            [['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', 'A', 'L', 'G', 'O', 'R', 'I', 'T', 'M', 'O', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', 'P', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', 'R', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', 'O', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', 'G', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', 'R', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', 'A', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', 'M', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', 'A', '.', '.', '.', '.', 'T', '.', '.', '.'],
            ['C', 'O', 'M', 'P', 'U', 'T', 'A', 'D', 'O', 'R', '.', 'I', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'P', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'O', '.', '.', '.']]
        conj_letras1 = fp.cria_conjunto(('M', 'A', 'S', 'L'),(2,1,3,1))
        assert fp.joga_palavra(tab, 'MOLA', fp.cria_casa(12,2), 'V', conj_letras1, False) == ('A', 'L', 'M') and \
            fp.obtem_sequencia(tab, (12,2), 'V', len('MOLA')) == 'MOLA' and \
                conj_letras1 == fp.cria_conjunto(('M', 'A', 'S', 'L'),(2,1,3,1))
    
    def test_13(self):
        tab = \
            [['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', 'A', 'L', 'G', 'O', 'R', 'I', 'T', 'M', 'O', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', 'P', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', 'R', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', 'O', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', 'G', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', 'R', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', 'A', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', 'M', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', 'A', '.', '.', '.', '.', 'T', '.', '.', '.'],
            ['C', 'O', 'M', 'P', 'U', 'T', 'A', 'D', 'O', 'R', '.', 'I', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'P', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'O', '.', '.', '.']]
        conj_letras1 = fp.cria_conjunto(('M', 'A', 'S', 'L'),(2,1,3,1))
        assert fp.joga_palavra(tab, 'MOLAS', fp.cria_casa(12,2), 'V', conj_letras1, False) == () and \
            fp.obtem_sequencia(tab, (12,2), 'V', len('MOLA')) == '.O..' and \
                conj_letras1 == fp.cria_conjunto(('M', 'A', 'S', 'L'),(2,1,3,1))
    
    def test_14(self):
        tab = \
            [['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', 'A', 'L', 'G', 'O', 'R', 'I', 'T', 'M', 'O', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', 'P', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', 'R', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', 'O', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', 'G', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', 'R', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', 'A', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', 'M', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', 'A', '.', '.', '.', '.', 'T', '.', '.', '.'],
            ['C', 'O', 'M', 'P', 'U', 'T', 'A', 'D', 'O', 'R', '.', 'I', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'P', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'O', '.', '.', '.']]
        conj_letras1 = fp.cria_conjunto(('R', 'A', 'T', 'O'),(2,1,3,1))
        assert fp.joga_palavra(tab, 'PATO', fp.cria_casa(14,12), 'H', conj_letras1, False) == ('A', 'O', 'T') and \
            fp.tabuleiro_para_str(tab) == \
"""                       1 1 1 1 1 1
     1 2 3 4 5 6 7 8 9 0 1 2 3 4 5
   +-------------------------------+
 1 | . . . . . . . . . . . . . . . |
 2 | . . A L G O R I T M O . . . . |
 3 | . . . . . . . . . . . . . . . |
 4 | . . . . . . . . . . . . . . . |
 5 | . . . . . . P . . . . . . . . |
 6 | . . . . . . R . . . . . . . . |
 7 | . . . . . . O . . . . . . . . |
 8 | . . . . . . G . . . . . . . . |
 9 | . . . . . . R . . . . . . . . |
10 | . . . . . . A . . . . . . . . |
11 | . . . . . . M . . . . . . . . |
12 | . . . . . . A . . . . T . . . |
13 | C O M P U T A D O R . I . . . |
14 | . . . . . . . . . . . P A T O |
15 | . . . . . . . . . . . O . . . |
   +-------------------------------+""" 
    
    def test_15(self):
        tab = \
            [['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', 'A', 'L', 'G', 'O', 'R', 'I', 'T', 'M', 'O', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', 'P', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', 'R', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', 'O', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', 'G', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', 'R', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', 'A', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', 'M', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', 'A', '.', '.', '.', '.', 'T', '.', '.', '.'],
            ['C', 'O', 'M', 'P', 'U', 'T', 'A', 'D', 'O', 'R', '.', 'I', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'P', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'O', '.', '.', '.']]
        conj_letras1 = fp.cria_conjunto(('R', 'A', 'T', 'O'),(2,1,3,1))
        assert fp.joga_palavra(tab, 'PRATO', fp.cria_casa(14,12), 'H', conj_letras1, False) == () and \
            fp.tabuleiro_para_str(tab) == \
"""                       1 1 1 1 1 1
     1 2 3 4 5 6 7 8 9 0 1 2 3 4 5
   +-------------------------------+
 1 | . . . . . . . . . . . . . . . |
 2 | . . A L G O R I T M O . . . . |
 3 | . . . . . . . . . . . . . . . |
 4 | . . . . . . . . . . . . . . . |
 5 | . . . . . . P . . . . . . . . |
 6 | . . . . . . R . . . . . . . . |
 7 | . . . . . . O . . . . . . . . |
 8 | . . . . . . G . . . . . . . . |
 9 | . . . . . . R . . . . . . . . |
10 | . . . . . . A . . . . . . . . |
11 | . . . . . . M . . . . . . . . |
12 | . . . . . . A . . . . T . . . |
13 | C O M P U T A D O R . I . . . |
14 | . . . . . . . . . . . P . . . |
15 | . . . . . . . . . . . O . . . |
   +-------------------------------+""" 
         
         
class TestProcessaJogada:
    def test_1(self):
        
        tab = fp.cria_tabuleiro()
        tab_str = fp.tabuleiro_para_str(tab)
        saco = ['S', 'B', 'P', 'E', 'C', 'E', 'E', 'S', 'J', 'I', 'D']
        saco_str = str(saco)
        jog1 = fp.cria_jogador(1, 0, fp.cria_conjunto(('A', 'U', 'O','T','X','F'),(2,1,1,1,1,1)))
        jog1_str = fp.jogador_para_str(jog1)
        
        res, text = False, 'Jogada J1: '
        assert processa_jogada_offline(tab, jog1, saco, LETRAS_PONTOS.copy(), True, "P\n") == (res, text) and \
           processa_jogada_offline(tab, jog1, saco, LETRAS_PONTOS.copy(), False, "P\n") == (res, text) and \
           tab_str == fp.tabuleiro_para_str(tab) and \
           saco_str == str(saco) and \
           jog1_str == fp.jogador_para_str(jog1) 

    def test_2(self):
        
        tab = fp.cria_tabuleiro()
        tab_str = fp.tabuleiro_para_str(tab)
        saco = ['S', 'B', 'P', 'E', 'C', 'E', 'E', 'S', 'J', 'I', 'D']
        saco_str = str(saco)
        jog1 = fp.cria_jogador(1, 0, fp.cria_conjunto(('A', 'U', 'O','T','X','F'),(2,1,1,1,1,1)))
        jog1_str = fp.jogador_para_str(jog1)
        
        res, text = False, 'Jogada J1: Jogada J1: '
        assert processa_jogada_offline(tab, jog1, saco, LETRAS_PONTOS.copy(), True, "J ? TUA\nP\n") == (res, text) and \
            processa_jogada_offline(tab, jog1, saco, LETRAS_PONTOS.copy(), False, "J ? TUA\nP\n") == (res, text) and \
           tab_str == fp.tabuleiro_para_str(tab) and \
           saco_str == str(saco) and \
           jog1_str == fp.jogador_para_str(jog1) 

    def test_3(self):
        
        tab = fp.cria_tabuleiro()
        tab_str = fp.tabuleiro_para_str(tab)
        saco = ['S', 'B', 'P', 'E', 'C', 'E', 'E', 'S', 'J', 'I', 'D']
        saco_str = str(saco)
        jog1 = fp.cria_jogador(1, 0, fp.cria_conjunto(('A', 'U', 'O','T','X','F'),(2,1,1,1,1,1)))
        jog1_str = fp.jogador_para_str(jog1)
        
        res, text = False, 'Jogada J1: Jogada J1: '
        assert processa_jogada_offline(tab, jog1, saco, LETRAS_PONTOS.copy(), True, "PASSA\nP\n") == (res, text) and \
            processa_jogada_offline(tab, jog1, saco, LETRAS_PONTOS.copy(), False, "PASSA\nP\n") == (res, text) and \
           tab_str == fp.tabuleiro_para_str(tab) and \
           saco_str == str(saco) and \
           jog1_str == fp.jogador_para_str(jog1) 
      
    
    def test_4(self):
        
        tab = fp.cria_tabuleiro()
        tab_str = fp.tabuleiro_para_str(tab)
        saco = ['S', 'B', 'P', 'E', 'C', 'E', 'E', 'S', 'J', 'I', 'D']
        saco_str = str(saco)
        jog1 = fp.cria_jogador(1, 0, fp.cria_conjunto(('A', 'U', 'O','T','X','F'),(2,1,1,1,1,1)))
        jog1_str = fp.jogador_para_str(jog1)
        
        res, text = False, 'Jogada J1: Jogada J1: Jogada J1: Jogada J1: Jogada J1: Jogada J1: '
        assert processa_jogada_offline(tab, jog1, saco, LETRAS_PONTOS.copy(), True, "12\nÇ\np\n?\n \nP\n") == (res, text) and \
            processa_jogada_offline(tab, jog1, saco, LETRAS_PONTOS.copy(), False, "12\nÇ\np\n?\n \nP\n") == (res, text) and \
           tab_str == fp.tabuleiro_para_str(tab) and \
           saco_str == str(saco) and \
           jog1_str == fp.jogador_para_str(jog1) 
                
    def test_5(self):
        
        tab = fp.cria_tabuleiro()
        tab_str = fp.tabuleiro_para_str(tab)
        saco = ['S', 'B', 'P', 'E', 'C', 'E', 'E', 'S', 'J', 'I', 'D']
        saco_str = str(saco)
        jog1 = fp.cria_jogador(1, 0, fp.cria_conjunto(('A', 'U', 'O','T','X','F'),(2,1,1,1,1,1)))
        jog1_str = fp.jogador_para_str(jog1)
        
        res, text = False, 'Jogada J1: Jogada J1: '
        assert processa_jogada_offline(tab, jog1, saco, LETRAS_PONTOS.copy(), True, "T 8\nP\n") == (res, text) and \
            processa_jogada_offline(tab, jog1, saco, LETRAS_PONTOS.copy(), False, "T 8\nP\n") == (res, text) and \
           tab_str == fp.tabuleiro_para_str(tab) and \
           saco_str == str(saco) and \
           jog1_str == fp.jogador_para_str(jog1) 
           
    def test_6(self):
        
        tab = fp.cria_tabuleiro()
        tab_str = fp.tabuleiro_para_str(tab)
        saco = ['S', 'B', 'P', 'E', 'C', 'E', 'E', 'S', 'J', 'I', 'D']
        saco_str = str(saco)
        jog1 = fp.cria_jogador(1, 0, fp.cria_conjunto(('A', 'U', 'O','T','X','F'),(2,1,1,1,1,1)))
        jog1_str = fp.jogador_para_str(jog1)
        
        res, text = False, 'Jogada J1: Jogada J1: '
        assert processa_jogada_offline(tab, jog1, saco, LETRAS_PONTOS.copy(), True, "T A A A O\nP\n") == (res, text) and \
            processa_jogada_offline(tab, jog1, saco, LETRAS_PONTOS.copy(), False, "T A A A O\nP\n") == (res, text) and \
           tab_str == fp.tabuleiro_para_str(tab) and \
           saco_str == str(saco) and \
           jog1_str == fp.jogador_para_str(jog1) 

    def test_7(self):
        
        tab = fp.cria_tabuleiro()
        tab_str = fp.tabuleiro_para_str(tab)
        saco = ['S', 'B', 'P', 'E', 'C']
        saco_str = str(saco)
        jog1 = fp.cria_jogador(1, 0, fp.cria_conjunto(('A', 'U', 'O','T','X','F'),(2,1,1,1,1,1)))
        jog1_str = fp.jogador_para_str(jog1)
        
        res, text = False, 'Jogada J1: Jogada J1: '
        assert processa_jogada_offline(tab, jog1, saco, LETRAS_PONTOS.copy(), True, "T A A O\nP\n") == (res, text) and \
            processa_jogada_offline(tab, jog1, saco, LETRAS_PONTOS.copy(), False, "T A A O\nP\n") == (res, text) and \
           tab_str == fp.tabuleiro_para_str(tab) and \
           saco_str == str(saco) and \
           jog1_str == fp.jogador_para_str(jog1) 


    def test_8(self):
     
        tab = fp.cria_tabuleiro()
        saco = ['S', 'B', 'P', 'E', 'C', 'E', 'E', 'S', 'J', 'I', 'D']
        jog1 = fp.cria_jogador(2, 10, fp.cria_conjunto(('E', 'I', 'O','S','X','G'),(2,1,1,1,1,1)))
        
        tab_str = fp.tabuleiro_para_str(tab)
        
        res, text = True, 'Jogada J2: '
        assert processa_jogada_offline(tab, jog1, saco, LETRAS_PONTOS.copy(), False, "T E I E\n") == (res, text) and \
            fp.jogador_para_str(jog1) == '#2 ( 10): D G I J O S X'  and \
                tab_str == fp.tabuleiro_para_str(tab) and \
                    saco == ['S', 'B', 'P', 'E', 'C', 'E', 'E', 'S'] 

    def test_9(self):
     
        tab = fp.cria_tabuleiro()
        saco = ['S', 'B', 'P', 'E', 'C', 'E', 'E', 'S', 'J', 'I', 'D']
        jog1 = fp.cria_jogador(2, 10, fp.cria_conjunto(('E', 'I', 'O','S','X','G'),(2,1,1,1,1,1)))
        
        tab_str = fp.tabuleiro_para_str(tab)
        
        res, text = True, 'Jogada J2: '
        assert processa_jogada_offline(tab, jog1, saco, LETRAS_PONTOS.copy(), True, "T E I E\n") == (res, text) and \
            fp.jogador_para_str(jog1) == '#2 ( 10): D G I J O S X'  and \
                tab_str == fp.tabuleiro_para_str(tab) and \
                    saco == ['S', 'B', 'P', 'E', 'C', 'E', 'E', 'S'] 

    ######
    # COMPLATAR CON JUGADAS INVaLIDAS Y VALIDAS DE JOGADA ANTERIORES
    ######
    def test_10(self):
        tab = fp.cria_tabuleiro()
        tab_str = fp.tabuleiro_para_str(tab)
        saco = ['S', 'B', 'P', 'E', 'C']
        saco_str = str(saco)
        jog1 = fp.cria_jogador(1, 0, fp.cria_conjunto(('M', 'E', 'A', 'L'), (2,1,3,1)))
        jog1_str = fp.jogador_para_str(jog1)
        
        res, text = False, 'Jogada J1: Jogada J1: '
        assert processa_jogada_offline(tab, jog1, saco, LETRAS_PONTOS.copy(), True, "J 7 7 V MEL\nP\n") == (res, text) and \
           tab_str == fp.tabuleiro_para_str(tab) and \
           saco_str == str(saco) and \
           jog1_str == fp.jogador_para_str(jog1) 
           

    def test_11(self):
        tab = fp.cria_tabuleiro()
        saco = ['S', 'B', 'P', 'E', 'C']
        jog1 = fp.cria_jogador(3, 0, fp.cria_conjunto(('M', 'E', 'A', 'L'), (2,1,3,1)))
        
        res, text = True, 'Jogada J3: '
        assert processa_jogada_offline(tab, jog1, saco, LETRAS_PONTOS.copy(), True, "J 7 8 V MEL\n") == (res, text) and \
           fp.obtem_sequencia(tab, (7,8), 'V', len('MEL')) == 'MEL' and \
           saco == ['S', 'B'] and \
           fp.jogador_para_str(jog1) == "#3 (  4): A A A C E M P"
           
    
    def test_12(self):
        tab = fp.cria_tabuleiro()
        saco = ['S', 'B']
        jog1 = fp.cria_jogador(4, 17, fp.cria_conjunto(('M', 'E', 'A', 'L'), (2,1,3,1)))
        
        res, text = True, 'Jogada J4: '
        assert processa_jogada_offline(tab, jog1, saco, LETRAS_PONTOS.copy(), True, "J 5 8 V MALA\n") == (res, text) and \
           fp.obtem_sequencia(tab, (4,8), 'V', len('.MALA.')) == '.MALA.' and \
           not saco and \
           fp.jogador_para_str(jog1) == "#4 ( 22): A B E M S"
           
    def test_13(self):
        tab = fp.cria_tabuleiro()
        tab_str = fp.tabuleiro_para_str(tab)
        saco = ['S', 'B', 'P', 'E', 'C']
        saco_str = str(saco)
        jog1 = fp.cria_jogador(2, 0, fp.cria_conjunto(('M', 'E', 'A', 'L'), (2,1,1,3)))
        jog1_str = fp.jogador_para_str(jog1)
        
        res, text = False, 'Jogada J2: Jogada J2: '
        assert processa_jogada_offline(tab, jog1, saco, LETRAS_PONTOS.copy(), True, "J 8 8 V LAMA\nP\n") == (res, text) and \
           tab_str == fp.tabuleiro_para_str(tab) and \
           saco_str == str(saco) and \
           jog1_str == fp.jogador_para_str(jog1) 
           
    def test_14(self):
        tab = fp.cria_tabuleiro()
        tab_str = fp.tabuleiro_para_str(tab)
        saco = ['S', 'B', 'P', 'E', 'C']
        saco_str = str(saco)
        jog1 = fp.cria_jogador(2, 0, fp.cria_conjunto(('C', 'A', 'O', 'N'),(2,1,3,1)))
        jog1_str = fp.jogador_para_str(jog1)
        
        res, text = False, 'Jogada J2: Jogada J2: '
        assert processa_jogada_offline(tab, jog1, saco, LETRAS_PONTOS.copy(), True, "J 8 8 H NOTA\nP\n") == (res, text) and \
           tab_str == fp.tabuleiro_para_str(tab) and \
           saco_str == str(saco) and \
           jog1_str == fp.jogador_para_str(jog1) 
      
      
    def test_15(self):
        tab = fp.cria_tabuleiro()
        tab_str = fp.tabuleiro_para_str(tab)
        saco = ['S', 'B', 'P', 'E', 'C']
        saco_str = str(saco)
        jog1 = fp.cria_jogador(3, 0, fp.cria_conjunto(('C', 'A', 'O', 'N'),(2,1,3,1)))
        jog1_str = fp.jogador_para_str(jog1)
        
        res, text = False, 'Jogada J3: Jogada J3: '
        assert processa_jogada_offline(tab, jog1, saco, LETRAS_PONTOS.copy(), False, "J 8 8 H NAO\nP\n") == (res, text) and \
           tab_str == fp.tabuleiro_para_str(tab) and \
           saco_str == str(saco) and \
           jog1_str == fp.jogador_para_str(jog1) 
          
    def test_16(self):
        tab = fp.cria_tabuleiro()
        fp.insere_palavra(tab, fp.cria_casa(8,8), 'H', 'NAO')
        tab_str = fp.tabuleiro_para_str(tab)
        saco = ['S', 'B', 'P', 'E', 'C']
        saco_str = str(saco)
        jog1 = fp.cria_jogador(3, 0, fp.cria_conjunto(('O', 'I', 'S', 'R', 'A'),(2,1,2,1,1)))
        jog1_str = fp.jogador_para_str(jog1)
        
        res, text = False, 'Jogada J3: Jogada J3: '
        assert processa_jogada_offline(tab, jog1, saco, LETRAS_PONTOS.copy(), False, "J 11 11 V RISO\nP\n") == (res, text) and \
           tab_str == fp.tabuleiro_para_str(tab) and \
           saco_str == str(saco) and \
           jog1_str == fp.jogador_para_str(jog1) 
   
         
    def test_17(self):
        tab = fp.cria_tabuleiro()
        fp.insere_palavra(tab, fp.cria_casa(8,8), 'H', 'NAO')
        saco = ['S', 'B', 'P', 'E', 'C', 'D', 'J', 'I']
        jog1 = fp.cria_jogador(3, 13, fp.cria_conjunto(('O', 'I', 'S', 'R', 'A'),(2,1,2,1,1)))
        
        res, text = True, 'Jogada J3: '
        assert processa_jogada_offline(tab, jog1, saco, LETRAS_PONTOS.copy(), False, "J 5 10 V RISO\n") == (res, text) and \
        fp.obtem_sequencia(tab, (5,10), 'V', len('RISO')) == 'RISO' and \
           saco == ['S', 'B', 'P', 'E', 'C'] and \
           fp.jogador_para_str(jog1) == "#3 ( 17): A D I J O O S"
   

  
    def test_18(self):
        tab = fp.cria_tabuleiro()
        fp.insere_palavra(tab, fp.cria_casa(8,8), 'H', 'NAO')
        saco = ['S', 'B', 'P', 'E', 'C', 'D', 'J', 'I']
        jog1 = fp.cria_jogador(2, 13, fp.cria_conjunto(('O', 'I', 'S', 'R', 'A'),(2,1,2,1,1)))
        
        res, text = True, 'Jogada J2: '
        assert processa_jogada_offline(tab, jog1, saco, LETRAS_PONTOS.copy(), False, "J 8 9 V AO\n") == (res, text) and \
        fp.obtem_sequencia(tab, (8,9), 'V', len('AO')) == 'AO' and \
           saco == ['S', 'B', 'P', 'E', 'C', 'D', 'J'] and \
           fp.jogador_para_str(jog1) == "#2 ( 15): A I I O R S S"
   
   
    def test_19(self):
        tab = fp.cria_tabuleiro()
        fp.insere_palavra(tab, fp.cria_casa(8,8), 'H', 'NAO')
        saco = ['S', 'B', 'P', 'E', 'C', 'D', 'J', 'I']
        jog1 = fp.cria_jogador(2, 13, fp.cria_conjunto(('O', 'I', 'S', 'R', 'A'),(2,1,2,1,1)))
        tab_str = fp.tabuleiro_para_str(tab)
        saco_str = str(saco)
        jog1_str = fp.jogador_para_str(jog1)
        
        res, text = False, 'Jogada J2: Jogada J2: '
        assert processa_jogada_offline(tab, jog1, saco, LETRAS_PONTOS.copy(), False, "J 8 9 H AO\nP\n") == (res, text) and \
        tab_str == fp.tabuleiro_para_str(tab) and \
           saco_str == str(saco) and \
           jog1_str == fp.jogador_para_str(jog1) 
  
    
  
    def test_20(self):
        tab = \
            [['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', 'A', 'L', 'G', 'O', 'R', 'I', 'T', 'M', 'O', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', 'P', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', 'R', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', 'O', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', 'G', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', 'R', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', 'A', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', 'M', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', 'A', '.', '.', '.', '.', 'T', '.', '.', '.'],
            ['C', 'O', 'M', 'P', 'U', 'T', 'A', 'D', 'O', 'R', '.', 'I', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'P', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'O', '.', '.', '.']]
        
        saco = [ 'C', 'D', 'J', 'I', 'S', 'B', 'P', 'E']
        jog1 = fp.cria_jogador(1, 25, fp.cria_conjunto(('M', 'A', 'S', 'L'),(2,1,3,1)))
        
        res, text = True, 'Jogada J1: '
        assert processa_jogada_offline(tab, jog1, saco, LETRAS_PONTOS.copy(), False, "J 12 2 V MOLA\n") == (res, text) and \
        fp.obtem_sequencia(tab, (12,2), 'V', len('MOLA')) == 'MOLA' and \
           saco == ['C', 'D', 'J', 'I', 'S'] and \
           fp.jogador_para_str(jog1) == "#1 ( 30): B E M P S S S"
   
   
    def test_21(self):
        tab = \
            [['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', 'A', 'L', 'G', 'O', 'R', 'I', 'T', 'M', 'O', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', 'P', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', 'R', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', 'O', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', 'G', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', 'R', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', 'A', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', 'M', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', 'A', '.', '.', '.', '.', 'T', '.', '.', '.'],
            ['C', 'O', 'M', 'P', 'U', 'T', 'A', 'D', 'O', 'R', '.', 'I', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'P', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'O', '.', '.', '.']]
        
        saco = [ 'C', 'D', 'J', 'I', 'S', 'B', 'P', 'E']
        jog1 = fp.cria_jogador(1, 25, fp.cria_conjunto(('M', 'A', 'S', 'L'),(2,1,3,1)))
        
        tab_str = fp.tabuleiro_para_str(tab)
        saco_str = str(saco)
        jog1_str = fp.jogador_para_str(jog1)
        
        res, text = False, 'Jogada J1: Jogada J1: '
        assert processa_jogada_offline(tab, jog1, saco, LETRAS_PONTOS.copy(), False, "J 12 2 V MOLAS\nP\n") == (res, text) and \
        tab_str == fp.tabuleiro_para_str(tab) and \
           saco_str == str(saco) and \
           jog1_str == fp.jogador_para_str(jog1) 
  
    
    def test_22(self):
        tab = \
            [['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', 'A', 'L', 'G', 'O', 'R', 'I', 'T', 'M', 'O', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', 'P', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', 'R', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', 'O', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', 'G', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', 'R', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', 'A', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', 'M', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', 'A', '.', '.', '.', '.', 'T', '.', '.', '.'],
            ['C', 'O', 'M', 'P', 'U', 'T', 'A', 'D', 'O', 'R', '.', 'I', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'P', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'O', '.', '.', '.']]
        
        saco = [ 'C', 'D', 'J', 'I', 'S', 'B', 'P', 'E']
        jog1 = fp.cria_jogador(1, 25, fp.cria_conjunto(('R', 'A', 'T', 'O'),(2,1,3,1)))
        
        tab_str = fp.tabuleiro_para_str(tab)
        saco_str = str(saco)
        jog1_str = fp.jogador_para_str(jog1)
        
        res, text = False, 'Jogada J1: Jogada J1: '
        assert processa_jogada_offline(tab, jog1, saco, LETRAS_PONTOS.copy(), False, "J 14 12 H PRATO\nP\n") == (res, text) and \
        tab_str == fp.tabuleiro_para_str(tab) and \
           saco_str == str(saco) and \
           jog1_str == fp.jogador_para_str(jog1) 
  
    
    
    def test_23(self):
        tab = \
            [['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', 'A', 'L', 'G', 'O', 'R', 'I', 'T', 'M', 'O', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', 'P', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', 'R', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', 'O', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', 'G', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', 'R', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', 'A', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', 'M', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', 'A', '.', '.', '.', '.', 'T', '.', '.', '.'],
            ['C', 'O', 'M', 'P', 'U', 'T', 'A', 'D', 'O', 'R', '.', 'I', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'P', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'O', '.', '.', '.']]
        
        saco = [ 'C', 'D', 'J', 'I', 'S', 'B', 'P', 'E']
        jog1 = fp.cria_jogador(1, 25, fp.cria_conjunto(('R', 'A', 'T', 'O'),(2,1,3,1)))
        
        res, text = True, 'Jogada J1: '
        assert processa_jogada_offline(tab, jog1, saco, LETRAS_PONTOS.copy(), False, "J 14 12 H PATO\n") == (res, text) and \
           saco == ['C', 'D', 'J', 'I', 'S'] and \
           fp.jogador_para_str(jog1) == "#1 ( 30): B E P R R T T" and \
               fp.tabuleiro_para_str(tab) == \
"""                       1 1 1 1 1 1
     1 2 3 4 5 6 7 8 9 0 1 2 3 4 5
   +-------------------------------+
 1 | . . . . . . . . . . . . . . . |
 2 | . . A L G O R I T M O . . . . |
 3 | . . . . . . . . . . . . . . . |
 4 | . . . . . . . . . . . . . . . |
 5 | . . . . . . P . . . . . . . . |
 6 | . . . . . . R . . . . . . . . |
 7 | . . . . . . O . . . . . . . . |
 8 | . . . . . . G . . . . . . . . |
 9 | . . . . . . R . . . . . . . . |
10 | . . . . . . A . . . . . . . . |
11 | . . . . . . M . . . . . . . . |
12 | . . . . . . A . . . . T . . . |
13 | C O M P U T A D O R . I . . . |
14 | . . . . . . . . . . . P A T O |
15 | . . . . . . . . . . . O . . . |
   +-------------------------------+"""  
 
    def test_24(self):

        tab = fp.cria_tabuleiro()
        saco = ['S', 'B', 'P', 'E', 'C', 'E', 'E', 'S', 'J']
        jog1 = fp.cria_jogador(1, 0, fp.cria_conjunto(('A', 'D', 'U','O','T','I','F'),(1,1,1,1,1,1,1)))
        
        
        res, text = True, 'Jogada J1: Jogada J1: '
        assert processa_jogada_offline(tab, jog1, saco, LETRAS_PONTOS.copy(), True, "J 7 8 V LUTA\nJ 7 8 V TOFU\n") == (res, text) and \
            fp.jogador_para_str(jog1) == '#1 (  7): A D E E I J S' and \
                saco == ['S', 'B', 'P', 'E', 'C']
      
      
      
class TestScrabble:
    def test_1(self):
        pontos = LETRAS_PONTOS.copy()

        saco = {
        "A": 14, "B": 3, "C": 4, "Ç": 2, "D": 5, "E": 11, "F": 2, "G": 2, "H": 2,
        "I": 10, "J": 2, "L": 5, "M": 6, "N": 4, "O": 10, "P": 4, "Q": 1,
        "R": 6, "S": 8, "T": 5, "U": 7, "V": 2, "X": 1, "Z": 1 }
        
        res = (21, 29)
        assert scrabble_offline(2, saco, pontos,  325, JOGADA_PRIVATE_1) == (res, OUTPUT_PRIVATE_1) 

    def test_2(self):
        pontos = LETRAS_PONTOS.copy()

        saco = {
        "A": 7, "L": 3, "M": 4}
        
        res = (9, 5)
        assert scrabble_offline(2, saco, pontos,  666, JOGADA_PRIVATE_2) == (res, OUTPUT_PRIVATE_2) 


    def test_3(self):
        pontos = LETRAS_PONTOS.copy()

        saco = {
        "A": 14, "B": 3, "C": 4, "Ç": 2, "D": 5, "E": 11, "F": 2, "G": 2, "H": 2,
        "I": 10, "J": 2, "L": 5, "M": 6, "N": 4, "O": 10, "P": 4, "Q": 1,
        "R": 6, "S": 8, "T": 5, "U": 7, "V": 2, "X": 1, "Z": 1 }
        
        res = (12, 14)
        assert scrabble_offline(2, saco, pontos,  33, JOGADA_PRIVATE_3) == (res, OUTPUT_PRIVATE_3) 
    
    def test_4(self):
        pontos = LETRAS_PONTOS.copy()

        saco = {
        "A": 14, "B": 3, "C": 4, "Ç": 2, "D": 5, "E": 11, "F": 2, "G": 2, "H": 2,
        "I": 10, "J": 2, "L": 5, "M": 6, "N": 4, "O": 10, "P": 4, "Q": 1,
        "R": 6, "S": 8, "T": 5, "U": 7, "V": 2, "X": 1, "Z": 1 }
        
        res = (19, 13, 6, 6)
        assert scrabble_offline(4, saco, pontos,  1979, JOGADA_PRIVATE_4) == (res, OUTPUT_PRIVATE_4) 
            
class TestScrabbleExceptions:
    def test_1(self):
        with pytest.raises(ValueError) as excinfo:
            pontos = LETRAS_PONTOS.copy()

            saco = {
            "A": 14, "B": 3, "C": 4, "Ç": 2, "D": 5, "E": 11, "F": 2, "G": 2, "H": 2,
            "I": 10, "J": 2, "L": 5, "M": 6, "N": 4, "O": 10, "P": 4, "Q": 1,
            "R": 6, "S": 8, "T": 5, "U": 7, "V": 2, "X": 1, "Z": 1 }
            
            scrabble_offline(2, saco, pontos,  33.0, JOGADA_PRIVATE_1)
        assert "scrabble: argumentos inválidos" == str(excinfo.value)
        
    def test_2(self):
        pontos = {
            "A": 1, "B": 3, "C": 2, "Ç": 3, "D": 2, "E": 1, "F": 4, "G": 4, "H": 4,
            "I": 1, "J": 5, "L": 2, "M": 1, "N": 3, "O": 1, "P": 2, "Q": 6,
            "R": 1, "S": 1, "T": 1, "U": 1, "V": 4, "X": 8 }


        saco = {
        "A": 14, "B": 3, "C": 4, "Ç": 2, "D": 5, "E": 11, "F": 2, "G": 2, "H": 2,
        "I": 10, "J": 2, "L": 5, "M": 6, "N": 4, "O": 10, "P": 4, "Q": 1,
        "R": 6, "S": 8, "T": 5, "U": 7, "V": 2, "X": 1, "Z": 1 }
        
        
        with pytest.raises(ValueError) as excinfo:
            scrabble_offline(2, saco, pontos,  33, JOGADA_PRIVATE_1)
        assert "scrabble: argumentos inválidos" == str(excinfo.value)
    
    
    def test_3(self):
        with pytest.raises(ValueError) as excinfo:
            pontos = LETRAS_PONTOS.copy()

            saco = {
            "A": 14, "B": 3, "C": 4, "Ç": 2, "D": 5, "E": 11, "F": 2, "G": 2, "H": 2,
            "I": 10, "J": 2, "L": 5, "M": 6, "N": 4, "O": 10, "P": 4, "Q": 1,
            "R": 6, "S": 8, "T": 5, "U": 7, "V": 2, "X": 1, "Z": 1 }
            
            scrabble_offline(5, saco, pontos,  33, JOGADA_PRIVATE_1)
        assert "scrabble: argumentos inválidos" == str(excinfo.value)
    
    
    def test_4(self):
        with pytest.raises(ValueError) as excinfo:
            pontos = LETRAS_PONTOS.copy()

            saco = {
            "A": 14, "B": 3, "C": 4, "W": 1 }
            
            scrabble_offline(2, saco, pontos,  33, JOGADA_PRIVATE_1)
        assert "scrabble: argumentos inválidos" == str(excinfo.value)
    
    def test_5(self):
        with pytest.raises(ValueError) as excinfo:
            pontos = LETRAS_PONTOS.copy()

            saco = { }
            
            scrabble_offline(2, saco, pontos,  33, JOGADA_PRIVATE_1)
        assert "scrabble: argumentos inválidos" == str(excinfo.value)
    
    def test_6(self):
        with pytest.raises(ValueError) as excinfo:
            pontos = LETRAS_PONTOS.copy()

            saco = {
            "A": 14, "B": 3, "C": -4 }
            
            scrabble_offline(2, saco, pontos,  33, JOGADA_PRIVATE_1)
        assert "scrabble: argumentos inválidos" == str(excinfo.value)
         
    def test_7(self):
        with pytest.raises(ValueError) as excinfo:
            pontos = LETRAS_PONTOS.copy()
            pontos["A"] = 0

            saco = {
            "A": 14, "B": 3, "C": 4, "Ç": 2, "D": 5, "E": 11, "F": 2, "G": 2, "H": 2,
            "I": 10, "J": 2, "L": 5, "M": 6, "N": 4, "O": 10, "P": 4, "Q": 1,
            "R": 6, "S": 8, "T": 5, "U": 7, "V": 2, "X": 1, "Z": 1 }
            
            scrabble_offline(2, saco, pontos,  33, JOGADA_PRIVATE_1)
        assert "scrabble: argumentos inválidos" == str(excinfo.value)
    
    def test_8(self):
        with pytest.raises(ValueError) as excinfo:
            
            saco = {
            "A": 14, "B": 3, "C": 4, "Ç": 2, "D": 5, "E": 11, "F": 2, "G": 2, "H": 2,
            "I": 10, "J": 2, "L": 5, "M": 6, "N": 4, "O": 10, "P": 4, "Q": 1,
            "R": 6, "S": 8, "T": 5, "U": 7, "V": 2, "X": 1, "Z": 1 }
            
            scrabble_offline(2, saco, True,  33, JOGADA_PRIVATE_1)
        assert "scrabble: argumentos inválidos" == str(excinfo.value)
    
           
### AUXILIAR CODE NECESSARY TO REPLACE STANDARD INPUT 
class ReplaceStdIn:
    def __init__(self, input_handle):
        self.input = input_handle.split('\n')
        self.line = 0

    def readline(self):
        if len(self.input) == self.line:
            return ''
        result = self.input[self.line]
        self.line += 1
        return result

class ReplaceStdOut:
    def __init__(self):
        self.output = ''

    def write(self, s):
        self.output += s
        return len(s)

    def flush(self):
        return 


def processa_jogada_offline(tabuleiro, jogador, saco, letras_pontos, first, input_jogo):
    oldstdin = sys.stdin
    sys.stdin = ReplaceStdIn(input_handle=input_jogo)
    
    oldstdout, newstdout = sys.stdout,  ReplaceStdOut()
    sys.stdout = newstdout

    try:
        res = fp.processa_jogada(tabuleiro, jogador, saco, letras_pontos, first)
        text = newstdout.output
        return res, text
    except ValueError as e:
        raise e
    finally:
        sys.stdin = oldstdin
        sys.stdout = oldstdout
        

def scrabble_offline(num_jogadores, letras_contagem, letras_pontos, seed, input_jogo):
    oldstdin = sys.stdin
    sys.stdin = ReplaceStdIn(input_handle=input_jogo)
    
    oldstdout, newstdout = sys.stdout,  ReplaceStdOut()
    sys.stdout = newstdout

    try:
        res = fp.scrabble(num_jogadores, letras_contagem, letras_pontos, seed)
        text = newstdout.output
        return res, text
    except ValueError as e:
        raise e
    finally:
        sys.stdin = oldstdin
        sys.stdout = oldstdout

#CONSTANTES
LETRAS_PONTOS = {
            "A": 1, "B": 3, "C": 2, "Ç": 3, "D": 2, "E": 1, "F": 4, "G": 4, "H": 4,
            "I": 1, "J": 5, "L": 2, "M": 1, "N": 3, "O": 1, "P": 2, "Q": 6,
            "R": 1, "S": 1, "T": 1, "U": 1, "V": 4, "X": 8, "Z": 8 }

# JOGOS AUTOMATICOS
JOGADA_PRIVATE_3 = 'J 6 8 V RISO\nJ 8 4 H LEOES\nJ 6 6 H VIROU\nJ 6 4 V VALE\nP\nP\n'
OUTPUT_PRIVATE_3 = """Bem-vindo ao SCRABBLE.
                       1 1 1 1 1 1
     1 2 3 4 5 6 7 8 9 0 1 2 3 4 5
   +-------------------------------+
 1 | . . . . . . . . . . . . . . . |
 2 | . . . . . . . . . . . . . . . |
 3 | . . . . . . . . . . . . . . . |
 4 | . . . . . . . . . . . . . . . |
 5 | . . . . . . . . . . . . . . . |
 6 | . . . . . . . . . . . . . . . |
 7 | . . . . . . . . . . . . . . . |
 8 | . . . . . . . . . . . . . . . |
 9 | . . . . . . . . . . . . . . . |
10 | . . . . . . . . . . . . . . . |
11 | . . . . . . . . . . . . . . . |
12 | . . . . . . . . . . . . . . . |
13 | . . . . . . . . . . . . . . . |
14 | . . . . . . . . . . . . . . . |
15 | . . . . . . . . . . . . . . . |
   +-------------------------------+
#1 (  0): B G I O R S V
#2 (  0): A E E E L O V
Jogada J1:                        1 1 1 1 1 1
     1 2 3 4 5 6 7 8 9 0 1 2 3 4 5
   +-------------------------------+
 1 | . . . . . . . . . . . . . . . |
 2 | . . . . . . . . . . . . . . . |
 3 | . . . . . . . . . . . . . . . |
 4 | . . . . . . . . . . . . . . . |
 5 | . . . . . . . . . . . . . . . |
 6 | . . . . . . . R . . . . . . . |
 7 | . . . . . . . I . . . . . . . |
 8 | . . . . . . . S . . . . . . . |
 9 | . . . . . . . O . . . . . . . |
10 | . . . . . . . . . . . . . . . |
11 | . . . . . . . . . . . . . . . |
12 | . . . . . . . . . . . . . . . |
13 | . . . . . . . . . . . . . . . |
14 | . . . . . . . . . . . . . . . |
15 | . . . . . . . . . . . . . . . |
   +-------------------------------+
#1 (  4): B D G I O U V
#2 (  0): A E E E L O V
Jogada J2:                        1 1 1 1 1 1
     1 2 3 4 5 6 7 8 9 0 1 2 3 4 5
   +-------------------------------+
 1 | . . . . . . . . . . . . . . . |
 2 | . . . . . . . . . . . . . . . |
 3 | . . . . . . . . . . . . . . . |
 4 | . . . . . . . . . . . . . . . |
 5 | . . . . . . . . . . . . . . . |
 6 | . . . . . . . R . . . . . . . |
 7 | . . . . . . . I . . . . . . . |
 8 | . . . L E O E S . . . . . . . |
 9 | . . . . . . . O . . . . . . . |
10 | . . . . . . . . . . . . . . . |
11 | . . . . . . . . . . . . . . . |
12 | . . . . . . . . . . . . . . . |
13 | . . . . . . . . . . . . . . . |
14 | . . . . . . . . . . . . . . . |
15 | . . . . . . . . . . . . . . . |
   +-------------------------------+
#1 (  4): B D G I O U V
#2 (  6): A A E I O U V
Jogada J1:                        1 1 1 1 1 1
     1 2 3 4 5 6 7 8 9 0 1 2 3 4 5
   +-------------------------------+
 1 | . . . . . . . . . . . . . . . |
 2 | . . . . . . . . . . . . . . . |
 3 | . . . . . . . . . . . . . . . |
 4 | . . . . . . . . . . . . . . . |
 5 | . . . . . . . . . . . . . . . |
 6 | . . . . . V I R O U . . . . . |
 7 | . . . . . . . I . . . . . . . |
 8 | . . . L E O E S . . . . . . . |
 9 | . . . . . . . O . . . . . . . |
10 | . . . . . . . . . . . . . . . |
11 | . . . . . . . . . . . . . . . |
12 | . . . . . . . . . . . . . . . |
13 | . . . . . . . . . . . . . . . |
14 | . . . . . . . . . . . . . . . |
15 | . . . . . . . . . . . . . . . |
   +-------------------------------+
#1 ( 12): B C D E G O Z
#2 (  6): A A E I O U V
Jogada J2:                        1 1 1 1 1 1
     1 2 3 4 5 6 7 8 9 0 1 2 3 4 5
   +-------------------------------+
 1 | . . . . . . . . . . . . . . . |
 2 | . . . . . . . . . . . . . . . |
 3 | . . . . . . . . . . . . . . . |
 4 | . . . . . . . . . . . . . . . |
 5 | . . . . . . . . . . . . . . . |
 6 | . . . V . V I R O U . . . . . |
 7 | . . . A . . . I . . . . . . . |
 8 | . . . L E O E S . . . . . . . |
 9 | . . . E . . . O . . . . . . . |
10 | . . . . . . . . . . . . . . . |
11 | . . . . . . . . . . . . . . . |
12 | . . . . . . . . . . . . . . . |
13 | . . . . . . . . . . . . . . . |
14 | . . . . . . . . . . . . . . . |
15 | . . . . . . . . . . . . . . . |
   +-------------------------------+
#1 ( 12): B C D E G O Z
#2 ( 14): A I O O S U U
Jogada J1:                        1 1 1 1 1 1
     1 2 3 4 5 6 7 8 9 0 1 2 3 4 5
   +-------------------------------+
 1 | . . . . . . . . . . . . . . . |
 2 | . . . . . . . . . . . . . . . |
 3 | . . . . . . . . . . . . . . . |
 4 | . . . . . . . . . . . . . . . |
 5 | . . . . . . . . . . . . . . . |
 6 | . . . V . V I R O U . . . . . |
 7 | . . . A . . . I . . . . . . . |
 8 | . . . L E O E S . . . . . . . |
 9 | . . . E . . . O . . . . . . . |
10 | . . . . . . . . . . . . . . . |
11 | . . . . . . . . . . . . . . . |
12 | . . . . . . . . . . . . . . . |
13 | . . . . . . . . . . . . . . . |
14 | . . . . . . . . . . . . . . . |
15 | . . . . . . . . . . . . . . . |
   +-------------------------------+
#1 ( 12): B C D E G O Z
#2 ( 14): A I O O S U U
Jogada J2: """

JOGADA_PRIVATE_1 = ("J 8 6 H MEIA\nJ 5 8 V NARIZ\nJ 6 5 H GOÇA\n"
                    "J 5 9 V LIMAO\nT S S\nP\nJ 2 6 V GASTO\n"
                    "J 2 6 H GORDA\nP\nP\n")
OUTPUT_PRIVATE_1 = """Bem-vindo ao SCRABBLE.
                       1 1 1 1 1 1
     1 2 3 4 5 6 7 8 9 0 1 2 3 4 5
   +-------------------------------+
 1 | . . . . . . . . . . . . . . . |
 2 | . . . . . . . . . . . . . . . |
 3 | . . . . . . . . . . . . . . . |
 4 | . . . . . . . . . . . . . . . |
 5 | . . . . . . . . . . . . . . . |
 6 | . . . . . . . . . . . . . . . |
 7 | . . . . . . . . . . . . . . . |
 8 | . . . . . . . . . . . . . . . |
 9 | . . . . . . . . . . . . . . . |
10 | . . . . . . . . . . . . . . . |
11 | . . . . . . . . . . . . . . . |
12 | . . . . . . . . . . . . . . . |
13 | . . . . . . . . . . . . . . . |
14 | . . . . . . . . . . . . . . . |
15 | . . . . . . . . . . . . . . . |
   +-------------------------------+
#1 (  0): A D E G I M U
#2 (  0): A L N O R U Z
Jogada J1:                        1 1 1 1 1 1
     1 2 3 4 5 6 7 8 9 0 1 2 3 4 5
   +-------------------------------+
 1 | . . . . . . . . . . . . . . . |
 2 | . . . . . . . . . . . . . . . |
 3 | . . . . . . . . . . . . . . . |
 4 | . . . . . . . . . . . . . . . |
 5 | . . . . . . . . . . . . . . . |
 6 | . . . . . . . . . . . . . . . |
 7 | . . . . . . . . . . . . . . . |
 8 | . . . . . M E I A . . . . . . |
 9 | . . . . . . . . . . . . . . . |
10 | . . . . . . . . . . . . . . . |
11 | . . . . . . . . . . . . . . . |
12 | . . . . . . . . . . . . . . . |
13 | . . . . . . . . . . . . . . . |
14 | . . . . . . . . . . . . . . . |
15 | . . . . . . . . . . . . . . . |
   +-------------------------------+
#1 (  4): A Ç D G O S U
#2 (  0): A L N O R U Z
Jogada J2:                        1 1 1 1 1 1
     1 2 3 4 5 6 7 8 9 0 1 2 3 4 5
   +-------------------------------+
 1 | . . . . . . . . . . . . . . . |
 2 | . . . . . . . . . . . . . . . |
 3 | . . . . . . . . . . . . . . . |
 4 | . . . . . . . . . . . . . . . |
 5 | . . . . . . . N . . . . . . . |
 6 | . . . . . . . A . . . . . . . |
 7 | . . . . . . . R . . . . . . . |
 8 | . . . . . M E I A . . . . . . |
 9 | . . . . . . . Z . . . . . . . |
10 | . . . . . . . . . . . . . . . |
11 | . . . . . . . . . . . . . . . |
12 | . . . . . . . . . . . . . . . |
13 | . . . . . . . . . . . . . . . |
14 | . . . . . . . . . . . . . . . |
15 | . . . . . . . . . . . . . . . |
   +-------------------------------+
#1 (  4): A Ç D G O S U
#2 ( 14): D D I L M O U
Jogada J1:                        1 1 1 1 1 1
     1 2 3 4 5 6 7 8 9 0 1 2 3 4 5
   +-------------------------------+
 1 | . . . . . . . . . . . . . . . |
 2 | . . . . . . . . . . . . . . . |
 3 | . . . . . . . . . . . . . . . |
 4 | . . . . . . . . . . . . . . . |
 5 | . . . . . . . N . . . . . . . |
 6 | . . . . G O Ç A . . . . . . . |
 7 | . . . . . . . R . . . . . . . |
 8 | . . . . . M E I A . . . . . . |
 9 | . . . . . . . Z . . . . . . . |
10 | . . . . . . . . . . . . . . . |
11 | . . . . . . . . . . . . . . . |
12 | . . . . . . . . . . . . . . . |
13 | . . . . . . . . . . . . . . . |
14 | . . . . . . . . . . . . . . . |
15 | . . . . . . . . . . . . . . . |
   +-------------------------------+
#1 ( 13): A D G S S S U
#2 ( 14): D D I L M O U
Jogada J2:                        1 1 1 1 1 1
     1 2 3 4 5 6 7 8 9 0 1 2 3 4 5
   +-------------------------------+
 1 | . . . . . . . . . . . . . . . |
 2 | . . . . . . . . . . . . . . . |
 3 | . . . . . . . . . . . . . . . |
 4 | . . . . . . . . . . . . . . . |
 5 | . . . . . . . N L . . . . . . |
 6 | . . . . G O Ç A I . . . . . . |
 7 | . . . . . . . R M . . . . . . |
 8 | . . . . . M E I A . . . . . . |
 9 | . . . . . . . Z O . . . . . . |
10 | . . . . . . . . . . . . . . . |
11 | . . . . . . . . . . . . . . . |
12 | . . . . . . . . . . . . . . . |
13 | . . . . . . . . . . . . . . . |
14 | . . . . . . . . . . . . . . . |
15 | . . . . . . . . . . . . . . . |
   +-------------------------------+
#1 ( 13): A D G S S S U
#2 ( 20): A D D I O R U
Jogada J1:                        1 1 1 1 1 1
     1 2 3 4 5 6 7 8 9 0 1 2 3 4 5
   +-------------------------------+
 1 | . . . . . . . . . . . . . . . |
 2 | . . . . . . . . . . . . . . . |
 3 | . . . . . . . . . . . . . . . |
 4 | . . . . . . . . . . . . . . . |
 5 | . . . . . . . N L . . . . . . |
 6 | . . . . G O Ç A I . . . . . . |
 7 | . . . . . . . R M . . . . . . |
 8 | . . . . . M E I A . . . . . . |
 9 | . . . . . . . Z O . . . . . . |
10 | . . . . . . . . . . . . . . . |
11 | . . . . . . . . . . . . . . . |
12 | . . . . . . . . . . . . . . . |
13 | . . . . . . . . . . . . . . . |
14 | . . . . . . . . . . . . . . . |
15 | . . . . . . . . . . . . . . . |
   +-------------------------------+
#1 ( 13): A D G S S T U
#2 ( 20): A D D I O R U
Jogada J2:                        1 1 1 1 1 1
     1 2 3 4 5 6 7 8 9 0 1 2 3 4 5
   +-------------------------------+
 1 | . . . . . . . . . . . . . . . |
 2 | . . . . . . . . . . . . . . . |
 3 | . . . . . . . . . . . . . . . |
 4 | . . . . . . . . . . . . . . . |
 5 | . . . . . . . N L . . . . . . |
 6 | . . . . G O Ç A I . . . . . . |
 7 | . . . . . . . R M . . . . . . |
 8 | . . . . . M E I A . . . . . . |
 9 | . . . . . . . Z O . . . . . . |
10 | . . . . . . . . . . . . . . . |
11 | . . . . . . . . . . . . . . . |
12 | . . . . . . . . . . . . . . . |
13 | . . . . . . . . . . . . . . . |
14 | . . . . . . . . . . . . . . . |
15 | . . . . . . . . . . . . . . . |
   +-------------------------------+
#1 ( 13): A D G S S T U
#2 ( 20): A D D I O R U
Jogada J1:                        1 1 1 1 1 1
     1 2 3 4 5 6 7 8 9 0 1 2 3 4 5
   +-------------------------------+
 1 | . . . . . . . . . . . . . . . |
 2 | . . . . . G . . . . . . . . . |
 3 | . . . . . A . . . . . . . . . |
 4 | . . . . . S . . . . . . . . . |
 5 | . . . . . T . N L . . . . . . |
 6 | . . . . G O Ç A I . . . . . . |
 7 | . . . . . . . R M . . . . . . |
 8 | . . . . . M E I A . . . . . . |
 9 | . . . . . . . Z O . . . . . . |
10 | . . . . . . . . . . . . . . . |
11 | . . . . . . . . . . . . . . . |
12 | . . . . . . . . . . . . . . . |
13 | . . . . . . . . . . . . . . . |
14 | . . . . . . . . . . . . . . . |
15 | . . . . . . . . . . . . . . . |
   +-------------------------------+
#1 ( 21): C D E I N S U
#2 ( 20): A D D I O R U
Jogada J2:                        1 1 1 1 1 1
     1 2 3 4 5 6 7 8 9 0 1 2 3 4 5
   +-------------------------------+
 1 | . . . . . . . . . . . . . . . |
 2 | . . . . . G O R D A . . . . . |
 3 | . . . . . A . . . . . . . . . |
 4 | . . . . . S . . . . . . . . . |
 5 | . . . . . T . N L . . . . . . |
 6 | . . . . G O Ç A I . . . . . . |
 7 | . . . . . . . R M . . . . . . |
 8 | . . . . . M E I A . . . . . . |
 9 | . . . . . . . Z O . . . . . . |
10 | . . . . . . . . . . . . . . . |
11 | . . . . . . . . . . . . . . . |
12 | . . . . . . . . . . . . . . . |
13 | . . . . . . . . . . . . . . . |
14 | . . . . . . . . . . . . . . . |
15 | . . . . . . . . . . . . . . . |
   +-------------------------------+
#1 ( 21): C D E I N S U
#2 ( 29): A A D I O R U
Jogada J1:                        1 1 1 1 1 1
     1 2 3 4 5 6 7 8 9 0 1 2 3 4 5
   +-------------------------------+
 1 | . . . . . . . . . . . . . . . |
 2 | . . . . . G O R D A . . . . . |
 3 | . . . . . A . . . . . . . . . |
 4 | . . . . . S . . . . . . . . . |
 5 | . . . . . T . N L . . . . . . |
 6 | . . . . G O Ç A I . . . . . . |
 7 | . . . . . . . R M . . . . . . |
 8 | . . . . . M E I A . . . . . . |
 9 | . . . . . . . Z O . . . . . . |
10 | . . . . . . . . . . . . . . . |
11 | . . . . . . . . . . . . . . . |
12 | . . . . . . . . . . . . . . . |
13 | . . . . . . . . . . . . . . . |
14 | . . . . . . . . . . . . . . . |
15 | . . . . . . . . . . . . . . . |
   +-------------------------------+
#1 ( 21): C D E I N S U
#2 ( 29): A A D I O R U
Jogada J2: """

JOGADA_PRIVATE_2 = "J 8 8 V MALA\nJ 10 8 H LAMA\nJ 8 8 H MAMA\n"
OUTPUT_PRIVATE_2 = """Bem-vindo ao SCRABBLE.
                       1 1 1 1 1 1
     1 2 3 4 5 6 7 8 9 0 1 2 3 4 5
   +-------------------------------+
 1 | . . . . . . . . . . . . . . . |
 2 | . . . . . . . . . . . . . . . |
 3 | . . . . . . . . . . . . . . . |
 4 | . . . . . . . . . . . . . . . |
 5 | . . . . . . . . . . . . . . . |
 6 | . . . . . . . . . . . . . . . |
 7 | . . . . . . . . . . . . . . . |
 8 | . . . . . . . . . . . . . . . |
 9 | . . . . . . . . . . . . . . . |
10 | . . . . . . . . . . . . . . . |
11 | . . . . . . . . . . . . . . . |
12 | . . . . . . . . . . . . . . . |
13 | . . . . . . . . . . . . . . . |
14 | . . . . . . . . . . . . . . . |
15 | . . . . . . . . . . . . . . . |
   +-------------------------------+
#1 (  0): A A A A L M M
#2 (  0): A A A L L M M
Jogada J1:                        1 1 1 1 1 1
     1 2 3 4 5 6 7 8 9 0 1 2 3 4 5
   +-------------------------------+
 1 | . . . . . . . . . . . . . . . |
 2 | . . . . . . . . . . . . . . . |
 3 | . . . . . . . . . . . . . . . |
 4 | . . . . . . . . . . . . . . . |
 5 | . . . . . . . . . . . . . . . |
 6 | . . . . . . . . . . . . . . . |
 7 | . . . . . . . . . . . . . . . |
 8 | . . . . . . . M . . . . . . . |
 9 | . . . . . . . A . . . . . . . |
10 | . . . . . . . L . . . . . . . |
11 | . . . . . . . A . . . . . . . |
12 | . . . . . . . . . . . . . . . |
13 | . . . . . . . . . . . . . . . |
14 | . . . . . . . . . . . . . . . |
15 | . . . . . . . . . . . . . . . |
   +-------------------------------+
#1 (  5): A A M
#2 (  0): A A A L L M M
Jogada J2:                        1 1 1 1 1 1
     1 2 3 4 5 6 7 8 9 0 1 2 3 4 5
   +-------------------------------+
 1 | . . . . . . . . . . . . . . . |
 2 | . . . . . . . . . . . . . . . |
 3 | . . . . . . . . . . . . . . . |
 4 | . . . . . . . . . . . . . . . |
 5 | . . . . . . . . . . . . . . . |
 6 | . . . . . . . . . . . . . . . |
 7 | . . . . . . . . . . . . . . . |
 8 | . . . . . . . M . . . . . . . |
 9 | . . . . . . . A . . . . . . . |
10 | . . . . . . . L A M A . . . . |
11 | . . . . . . . A . . . . . . . |
12 | . . . . . . . . . . . . . . . |
13 | . . . . . . . . . . . . . . . |
14 | . . . . . . . . . . . . . . . |
15 | . . . . . . . . . . . . . . . |
   +-------------------------------+
#1 (  5): A A M
#2 (  5): A L L M
Jogada J1: """

JOGADA_PRIVATE_4 = \
"""J 6 7 V LENTO
J 6 8 V LENTO
T A B C
J 9 5 H BEATO
J 7 7 H CESTO
J 3 11 V LIMAO
J 4 8 H SEXI
J 6 8 H LULA
P
P
P
P"""

OUTPUT_PRIVATE_4 = \
"""Bem-vindo ao SCRABBLE.
                       1 1 1 1 1 1
     1 2 3 4 5 6 7 8 9 0 1 2 3 4 5
   +-------------------------------+
 1 | . . . . . . . . . . . . . . . |
 2 | . . . . . . . . . . . . . . . |
 3 | . . . . . . . . . . . . . . . |
 4 | . . . . . . . . . . . . . . . |
 5 | . . . . . . . . . . . . . . . |
 6 | . . . . . . . . . . . . . . . |
 7 | . . . . . . . . . . . . . . . |
 8 | . . . . . . . . . . . . . . . |
 9 | . . . . . . . . . . . . . . . |
10 | . . . . . . . . . . . . . . . |
11 | . . . . . . . . . . . . . . . |
12 | . . . . . . . . . . . . . . . |
13 | . . . . . . . . . . . . . . . |
14 | . . . . . . . . . . . . . . . |
15 | . . . . . . . . . . . . . . . |
   +-------------------------------+
#1 (  0): E L N O T U X
#2 (  0): A B E I O U U
#3 (  0): C O S T T U U
#4 (  0): A E E I I L M
Jogada J1: Jogada J1:                        1 1 1 1 1 1
     1 2 3 4 5 6 7 8 9 0 1 2 3 4 5
   +-------------------------------+
 1 | . . . . . . . . . . . . . . . |
 2 | . . . . . . . . . . . . . . . |
 3 | . . . . . . . . . . . . . . . |
 4 | . . . . . . . . . . . . . . . |
 5 | . . . . . . . . . . . . . . . |
 6 | . . . . . . . L . . . . . . . |
 7 | . . . . . . . E . . . . . . . |
 8 | . . . . . . . N . . . . . . . |
 9 | . . . . . . . T . . . . . . . |
10 | . . . . . . . O . . . . . . . |
11 | . . . . . . . . . . . . . . . |
12 | . . . . . . . . . . . . . . . |
13 | . . . . . . . . . . . . . . . |
14 | . . . . . . . . . . . . . . . |
15 | . . . . . . . . . . . . . . . |
   +-------------------------------+
#1 (  8): E I S U U V X
#2 (  0): A B E I O U U
#3 (  0): C O S T T U U
#4 (  0): A E E I I L M
Jogada J2: Jogada J2:                        1 1 1 1 1 1
     1 2 3 4 5 6 7 8 9 0 1 2 3 4 5
   +-------------------------------+
 1 | . . . . . . . . . . . . . . . |
 2 | . . . . . . . . . . . . . . . |
 3 | . . . . . . . . . . . . . . . |
 4 | . . . . . . . . . . . . . . . |
 5 | . . . . . . . . . . . . . . . |
 6 | . . . . . . . L . . . . . . . |
 7 | . . . . . . . E . . . . . . . |
 8 | . . . . . . . N . . . . . . . |
 9 | . . . . B E A T O . . . . . . |
10 | . . . . . . . O . . . . . . . |
11 | . . . . . . . . . . . . . . . |
12 | . . . . . . . . . . . . . . . |
13 | . . . . . . . . . . . . . . . |
14 | . . . . . . . . . . . . . . . |
15 | . . . . . . . . . . . . . . . |
   +-------------------------------+
#1 (  8): E I S U U V X
#2 (  7): A E I I L U U
#3 (  0): C O S T T U U
#4 (  0): A E E I I L M
Jogada J3:                        1 1 1 1 1 1
     1 2 3 4 5 6 7 8 9 0 1 2 3 4 5
   +-------------------------------+
 1 | . . . . . . . . . . . . . . . |
 2 | . . . . . . . . . . . . . . . |
 3 | . . . . . . . . . . . . . . . |
 4 | . . . . . . . . . . . . . . . |
 5 | . . . . . . . . . . . . . . . |
 6 | . . . . . . . L . . . . . . . |
 7 | . . . . . . C E S T O . . . . |
 8 | . . . . . . . N . . . . . . . |
 9 | . . . . B E A T O . . . . . . |
10 | . . . . . . . O . . . . . . . |
11 | . . . . . . . . . . . . . . . |
12 | . . . . . . . . . . . . . . . |
13 | . . . . . . . . . . . . . . . |
14 | . . . . . . . . . . . . . . . |
15 | . . . . . . . . . . . . . . . |
   +-------------------------------+
#1 (  8): E I S U U V X
#2 (  7): A E I I L U U
#3 (  6): A E O P T U U
#4 (  0): A E E I I L M
Jogada J4:                        1 1 1 1 1 1
     1 2 3 4 5 6 7 8 9 0 1 2 3 4 5
   +-------------------------------+
 1 | . . . . . . . . . . . . . . . |
 2 | . . . . . . . . . . . . . . . |
 3 | . . . . . . . . . . L . . . . |
 4 | . . . . . . . . . . I . . . . |
 5 | . . . . . . . . . . M . . . . |
 6 | . . . . . . . L . . A . . . . |
 7 | . . . . . . C E S T O . . . . |
 8 | . . . . . . . N . . . . . . . |
 9 | . . . . B E A T O . . . . . . |
10 | . . . . . . . O . . . . . . . |
11 | . . . . . . . . . . . . . . . |
12 | . . . . . . . . . . . . . . . |
13 | . . . . . . . . . . . . . . . |
14 | . . . . . . . . . . . . . . . |
15 | . . . . . . . . . . . . . . . |
   +-------------------------------+
#1 (  8): E I S U U V X
#2 (  7): A E I I L U U
#3 (  6): A E O P T U U
#4 (  6): B E E E I S T
Jogada J1:                        1 1 1 1 1 1
     1 2 3 4 5 6 7 8 9 0 1 2 3 4 5
   +-------------------------------+
 1 | . . . . . . . . . . . . . . . |
 2 | . . . . . . . . . . . . . . . |
 3 | . . . . . . . . . . L . . . . |
 4 | . . . . . . . S E X I . . . . |
 5 | . . . . . . . . . . M . . . . |
 6 | . . . . . . . L . . A . . . . |
 7 | . . . . . . C E S T O . . . . |
 8 | . . . . . . . N . . . . . . . |
 9 | . . . . B E A T O . . . . . . |
10 | . . . . . . . O . . . . . . . |
11 | . . . . . . . . . . . . . . . |
12 | . . . . . . . . . . . . . . . |
13 | . . . . . . . . . . . . . . . |
14 | . . . . . . . . . . . . . . . |
15 | . . . . . . . . . . . . . . . |
   +-------------------------------+
#1 ( 19): I N O S U U V
#2 (  7): A E I I L U U
#3 (  6): A E O P T U U
#4 (  6): B E E E I S T
Jogada J2:                        1 1 1 1 1 1
     1 2 3 4 5 6 7 8 9 0 1 2 3 4 5
   +-------------------------------+
 1 | . . . . . . . . . . . . . . . |
 2 | . . . . . . . . . . . . . . . |
 3 | . . . . . . . . . . L . . . . |
 4 | . . . . . . . S E X I . . . . |
 5 | . . . . . . . . . . M . . . . |
 6 | . . . . . . . L U L A . . . . |
 7 | . . . . . . C E S T O . . . . |
 8 | . . . . . . . N . . . . . . . |
 9 | . . . . B E A T O . . . . . . |
10 | . . . . . . . O . . . . . . . |
11 | . . . . . . . . . . . . . . . |
12 | . . . . . . . . . . . . . . . |
13 | . . . . . . . . . . . . . . . |
14 | . . . . . . . . . . . . . . . |
15 | . . . . . . . . . . . . . . . |
   +-------------------------------+
#1 ( 19): I N O S U U V
#2 ( 13): A A A E I I U
#3 (  6): A E O P T U U
#4 (  6): B E E E I S T
Jogada J3:                        1 1 1 1 1 1
     1 2 3 4 5 6 7 8 9 0 1 2 3 4 5
   +-------------------------------+
 1 | . . . . . . . . . . . . . . . |
 2 | . . . . . . . . . . . . . . . |
 3 | . . . . . . . . . . L . . . . |
 4 | . . . . . . . S E X I . . . . |
 5 | . . . . . . . . . . M . . . . |
 6 | . . . . . . . L U L A . . . . |
 7 | . . . . . . C E S T O . . . . |
 8 | . . . . . . . N . . . . . . . |
 9 | . . . . B E A T O . . . . . . |
10 | . . . . . . . O . . . . . . . |
11 | . . . . . . . . . . . . . . . |
12 | . . . . . . . . . . . . . . . |
13 | . . . . . . . . . . . . . . . |
14 | . . . . . . . . . . . . . . . |
15 | . . . . . . . . . . . . . . . |
   +-------------------------------+
#1 ( 19): I N O S U U V
#2 ( 13): A A A E I I U
#3 (  6): A E O P T U U
#4 (  6): B E E E I S T
Jogada J4:                        1 1 1 1 1 1
     1 2 3 4 5 6 7 8 9 0 1 2 3 4 5
   +-------------------------------+
 1 | . . . . . . . . . . . . . . . |
 2 | . . . . . . . . . . . . . . . |
 3 | . . . . . . . . . . L . . . . |
 4 | . . . . . . . S E X I . . . . |
 5 | . . . . . . . . . . M . . . . |
 6 | . . . . . . . L U L A . . . . |
 7 | . . . . . . C E S T O . . . . |
 8 | . . . . . . . N . . . . . . . |
 9 | . . . . B E A T O . . . . . . |
10 | . . . . . . . O . . . . . . . |
11 | . . . . . . . . . . . . . . . |
12 | . . . . . . . . . . . . . . . |
13 | . . . . . . . . . . . . . . . |
14 | . . . . . . . . . . . . . . . |
15 | . . . . . . . . . . . . . . . |
   +-------------------------------+
#1 ( 19): I N O S U U V
#2 ( 13): A A A E I I U
#3 (  6): A E O P T U U
#4 (  6): B E E E I S T
Jogada J1:                        1 1 1 1 1 1
     1 2 3 4 5 6 7 8 9 0 1 2 3 4 5
   +-------------------------------+
 1 | . . . . . . . . . . . . . . . |
 2 | . . . . . . . . . . . . . . . |
 3 | . . . . . . . . . . L . . . . |
 4 | . . . . . . . S E X I . . . . |
 5 | . . . . . . . . . . M . . . . |
 6 | . . . . . . . L U L A . . . . |
 7 | . . . . . . C E S T O . . . . |
 8 | . . . . . . . N . . . . . . . |
 9 | . . . . B E A T O . . . . . . |
10 | . . . . . . . O . . . . . . . |
11 | . . . . . . . . . . . . . . . |
12 | . . . . . . . . . . . . . . . |
13 | . . . . . . . . . . . . . . . |
14 | . . . . . . . . . . . . . . . |
15 | . . . . . . . . . . . . . . . |
   +-------------------------------+
#1 ( 19): I N O S U U V
#2 ( 13): A A A E I I U
#3 (  6): A E O P T U U
#4 (  6): B E E E I S T
Jogada J2: """
