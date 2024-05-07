import nmap

print("""**********************
Bienvenido al Scanner
**********************""")
scanner = nmap.PortScanner()
ip = input("Que ip desea escanear?\n")
respuesta = input("""
Seleccionar tipo de scaneo\n1 - Simple\n2 - Profesional
""")

if respuesta == "1":
    print("SCANEO SIMPLE")
    print("Nmap version: ", scanner.nmap_version())
    print(scanner.scan(ip, "1-1024", "-v"))
    print("Info: ", scanner.scaninfo())
    print("Estado IP: ", scanner[ip].state())
    print("Protocolos de esta IP: ",scanner[ip].all_protocols())
    print("Puertos abiertos detectados: ", scanner[ip]["tcp"].keys())
elif respuesta == "2":
    scanner.scan(ip, "1-1024", "-v -O -sV")
    print("************************************************")
    print("SCANEO PROFESIONAL")
    print("************************************************")
    scanner.scan(ip, "1-1024", "-v -O -sV")
    scanner.scaninfo() 
    protocolos= scanner[ip].all_protocols()
    for protocolo in protocolos:
        puertos= scanner[ip][protocolo].keys()
        for puerto in puertos:  
            print("PUERTO: ", puerto)
            print("SISTEMA OPERATIVO: ", scanner[ip][protocolo][puerto]["product"])
            print("VERSION: ", scanner[ip][protocolo][puerto]["version"])
            print("************************************************")

else:
    print("Por favor Seleccione una opción válida")