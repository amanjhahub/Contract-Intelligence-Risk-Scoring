def main_menu():

    while True:

        print("\n================================")
        print(" Contract Intelligence System")
        print("================================")

        print("\n1. Analyze Single Contract")
        print("2. Compare Two Contracts")
        print("3. Generate Summary")
        print("4. Exit")


        choice = input("\nEnter choice: ")


        if choice == "1":

            from main import run_single_contract

            run_single_contract()


        elif choice == "2":

         from comparison.run_comparison import run_comparison

         run_comparison()


        elif choice == "3":

         from summarizer.run_summary import run_summary

         run_summary()

        elif choice == "4":

            print("\nExiting...")
            break


        else:

            print("\nInvalid choice")


if __name__ == "__main__":

    main_menu()