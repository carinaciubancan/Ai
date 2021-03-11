#metoda returneaza numarul de locatii, sursa si destinatia, preluate din fisier
#primeste ca parametrii: matricea costurilor de la fiecare nod la altul si fisierul din care ia datele
def readFile(matrix, file):
    file = open(file, 'r')
    n = int(file.readline())
    for x in range(n):
        line = file.readline()
        lineValues = line.split(',')
        lineList = []

        for value in lineValues:
            lineList.append(int(value))
        matrix.append(lineList)

    s = int(file.readline())
    d = int(file.readline())

    return n,s,d

#metoda returneaza lungimea traseului, vectorul locatiilor si costul traseului, care este minim
#primeste ca parametrii: matricea costurilor de la fiecare nod la altul, numarul de locatii, sursa si destinatia
def gasesteTraseu(matrix, n, src, dest):
    
    traseu = [] 
    parcurse = [0]*(n+1) 
    parcurse[src] = 1 
    cost = 0 
    traseu.append(src) 
    
    for i in range(n):
        min = 999999999
        min_index = -1
        if len(traseu) != n:   
            for index in range(n): 
                if matrix[traseu[-1]-1][index] < min and parcurse[index+1] == 0 and matrix[traseu[-1]-1][index] != 0:
                    min = matrix[traseu[-1]-1][index] 
                    min_index = index + 1           
            
            cost += min
            traseu.append(min_index)   
            parcurse[min_index] = 1 
        if (min_index == dest): 
               break
    if(src==dest):
        cost += matrix[traseu[0] - 1][traseu[-1] - 1]

    return len(traseu),traseu,cost
  

def main():
    #file = 'easy_01_tsp.txt'        
    #file = 'easy_03_tsp.txt'
    #file = 'medium_01_tsp.txt'
    #file = 'hard_01_tsp.txt'
    #file = 'fisierEasy.txt'
    #file = 'fisierMedium.txt'
    #file = 'fisierHard.txt'

    #file = 'fisierUsor.txt'
    #file = 'fisierMediu.txt'
    file = 'fisierGreu.txt'

    output = 'output.txt'
    #file = 'fisierMediu.txt'
    #file = 'fisierGreu.txt'
    output = open(output,'w')

    mini=99999
    matrix = []
    n,s,d = readFile(matrix, file)

    n,vectr,cost=gasesteTraseu(matrix, n,1,1)

    output.write("Cerinta 1: \n")
    output.write("Cel mai scurt traseu care pleaca dintr-o locatie, viziteaza toate locatiile si revine in locatia de start\n")
    output.write(str(n))
    output.write("\n")
    output.write(str(vectr))
    output.write("\n")
    output.write(str(cost))
    output.write("\n")
    output.write("\n")

    m,vector,rez=gasesteTraseu(matrix,n,s,d)

    output.write("Cerinta 2: \n")
    output.write("Cel mai scurt traseu care pleaca dintr-o locatie si ajunge intr-o alta locatie, fiecare locatie din traseu fiind vizitata o singura data\n")
    output.write("Lungimea traseului este:")
    output.write( str(m))
    output.write("\n")
    output.write("Vectorul locatiilor este: ")
    output.write( str(vector))
    output.write("\n")
    output.write("Costul traseului este:")
    output.write( str(rez))

   
   
main()