def achaArquivo(documento,pagina):
    match documento:
        case "manual":
            pasta = "manual"
            match pagina:
                case 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8:
                    return f"{pasta}/nomedoarquivo1-8.txt"
                case 9 | 10 | 11 | 12 | 13 | 14:    
                    return "pasta/nomedoarquivo1-8.txt"
                case _:
                    return "n"
        case "PPC":
            pasta = "PPC"
            match pagina:
                case 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8:
                    return f"{pasta}/nomedoarquivo1-8.txt"
                case 9 | 10 | 11 | 12 | 13 | 14:    
                    return f"{pasta}/nomedoarquivo1-8.txt"
                case _:
                    return "n"
        case "Regimentno":
            pasta = "Regimentno"
            match pagina:
                case 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8:
                    return f"{pasta}/nomedoarquivo1-8.txt"
                case 9 | 10 | 11 | 12 | 13 | 14:    
                    return f"{pasta}/nomedoarquivo1-8.txt"
                case _: 
                    return "n"
        case _:
            return "n"

print(achaArquivo("manual", 5))   # Saída: manual/nomedoarquivo1-8.txt
print(achaArquivo("PPC", 10))     # Saída: PPC/nomedoarquivo9-14.txt
print(achaArquivo("Regimentno", 15))  # Saída: n
print(achaArquivo("outro", 5))   # Saída: n