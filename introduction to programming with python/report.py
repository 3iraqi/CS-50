def main():
    spacecraft={"name":"vogues"}
    spacecraft["distance"]="120"
    spacecraft.update({"age":"20"})
    print(create_report(spacecraft))
    
    
def create_report(spacecraft):
    return f"""
    ========= REPORT =========
    
    Name    : {spacecraft["name"]}
    Distance: {spacecraft.get("distance","UnKnown")} AU
    
    ==========================
    """
    
    
    
    
main()