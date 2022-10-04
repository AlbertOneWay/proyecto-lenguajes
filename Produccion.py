class Produccion:

    def __init__(self, noTerminals, inicial, productions):
        self.noTerminals = noTerminals
        self.inicial = inicial
        self.productions = productions

    def DeleteRecursionLeft(self):
        
        currentNoTerminal = self.inicial #S

        newProduction = []
        sameNoTerminal = False
        productionEmpty = []

        for production in self.productions:
          """["S", "S+P"]"""
          productions = self.productions[production]
          productionNew = []
          """aux = ['S','+','P']"""
          aux = productions[1].split(" ")

          if (currentNoTerminal != productions[0]):
                if (sameNoTerminal == True):
                    
                    productionEmpty.push("λ")
                    productionNew.push(productionEmpty)
                    productionEmpty = []
                
                currentNoTerminal = productions[0];
                sameNoTerminal = False;
            

          if(productions[0] == aux[0]):

                if(sameNoTerminal == False):
                    productionEmpty.push((productions[0]+"'"));
                
                sameNoTerminal = True;

                productionNew.push((productions[0]+"'")) #S'
                
                produc = ""

                for j in aux:
                  if(j == 0): #aux = ['S','+','P']
                    produc = aux[j+1] #+  
                    
                  else: 
                        if (j == len(aux)-1): 
                            produc = produc + " "+ productions[0]+"'" #S'
                        else: 
                            produc= produc +" "+ aux[j+1] #P
                
                productionNew.push(produc)
                newProduction.push(productionNew)

          else:
                 if (sameNoTerminal == True):
                    #indexOf si esta produccion dentro de producciones la devuelve y guarda en indice 
                    
                    #index = self.productions.index(produc)
                        indice = self.productions.indexOf(production)
                        

                        produc = productions[1]+" "+productions[0]+"'"
                        self.productions[indice][1] = produc

                 if (productions[0] == self.inicial):
            
            #unshift agrega uno o mas elementos al comienzo de una matriz y devuelve 
            # la nueva longitud de la matriz
            #productionNew.unshift(self.productions[index])
                        productionNew.unshift(self.productions[indice])
                 else:
                        #productionNew.push(self.productions[index])
                        productionNew.push(self.productions[indice])
                    
        else:
                    # Si no hay recursion por la izquierda guarda la produccion tal como estaba en 
                    # la nueva lista de producciones
                    #productionNew.push(production) or newProduction.push(production) 
                    productionNew.push(production);
          
                
                #S' -> + P S'

                #S -> F G S'| S + P 
                #S' -> + P S' | λ

         #S-> S + P 
                 
            
