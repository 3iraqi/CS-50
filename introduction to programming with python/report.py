def main():
    spacecraft={"name":"vogues","distance":"155"}
    print(create_report(spacecraft))
    
    
def create_report(spacecraft):
    return f"""
    ========= REPORT =========
    
    Name: {spacecraft["name"]}
    Distance: {spacecraft["distance"]}
    
    ==========================
    """
    
    
    
    
main()