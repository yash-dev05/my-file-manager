# Import all modules we created
import file_ops
import navigation
import search
import organizer

# Infinite loop so program keeps running
while True:

    print("\nSMART FILE MANAGER")
    print("1. List files")
    print("2. Create folder")
    print("3. Delete file/folder")
    print("4. Rename file")
    print("5. Copy file")
    print("6. Move file")
    print("7. Change directory")
    print("8. Show current directory")
    print("9. Search file")
    print("10. Organize folder")
    print("11. Exit")

    choice = input("\nEnter your choice: ")

    # Option 1: List files
    if choice == "1":
        path = input("Enter folder path: ")
        file_ops.list_files(path)

    # Option 2: Create folder
    elif choice == "2":
        path = input("Enter path: ")
        name = input("Folder name: ")
        file_ops.create_folder(path, name)

        # Option 3: Delete item
    elif choice == "3":
        path = input("Enter file/folder path: ")
        file_ops.delete_item(path)


    # Option 4: Rename
    elif choice == "4":
        old = input("Enter current name/path: ")
        new = input("Enter new name/path: ")
        file_ops.rename_item(old, new)


    # Option 5: Copy
    elif choice == "5":
        src = input("Enter source path: ")
        dest = input("Enter destination path: ")
        file_ops.copy_file(src, dest)


    # Option 6: Move
    elif choice == "6":
        src = input("Enter source path: ")
        dest = input("Enter destination path: ")
        file_ops.move_file(src, dest)


    # Option 7: Change directory
    elif choice == "7":
        path = input("Enter directory path: ")
        navigation.change_directory(path)


    # Option 8: Show current directory
    elif choice == "8":
        navigation.show_current_directory()


    # Option 9: Search file
    elif choice == "9":
        folder = input("Enter folder path: ")
        filename = input("Enter file name: ")
        search.search_file(folder, filename)


    # Option 10: Organize folder automatically
    elif choice == "10":
        path = input("Enter folder path: ")
        organizer.organize_folder(path)


    # Exit program
    elif choice == "11":
        print("Exiting Smart File Manager...")
        break


    else:
        print("Invalid choice. Try again.")



