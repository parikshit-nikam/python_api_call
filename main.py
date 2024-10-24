from api_client.builders.api_builder import ConcreteAPIBuilder

def main():
    builder = ConcreteAPIBuilder()
    client = builder.build_client()

    try:
        users = client.get_users()
        print("--------------------------------------------------------") 
        for user in users:
            print(f"Asset ID: {user.id}, \nName: {user.name}")
            
            if user.data:
                for key, value in user.data.root.items():
                    print(f"  • {key}: {value}")
            else:
                print("  • No additional data available.")

            print("--------------------------------------------------------")    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
