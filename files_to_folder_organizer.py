import os
import shutil

def organize_videos(video_directory):
    # List all files in the video directory
    files = os.listdir(video_directory)
    
    for file_name in files:
        # Check if the file is a video (you can add more extensions if needed)
        if file_name.endswith(('.mp4', '.avi', '.mov', '.mkv')):
            # Create a folder name based on the video file name without extension
            folder_name = os.path.splitext(file_name)[0]
            folder_path = os.path.join(video_directory, folder_name)
            
            # Create the new folder if it does not exist
            if not os.path.exists(folder_path):
                os.mkdir(folder_path)
            
            # Move the video file into the new folder
            shutil.move(os.path.join(video_directory, file_name), os.path.join(folder_path, file_name))
    
    print("Videos have been organized into their respective folders.")

def organize_videos_with_code(video_directory):
    # List all files in the video directory
    files = os.listdir(video_directory)
    
    for file_name in files:
        # Check if the file is a video or code (you can add more extensions if needed)
        if file_name.endswith(('.mp4', '.avi', '.mov', '.mkv')) or file_name.endswith('.py'):
            # Create a folder name based on the file name without extension
            folder_name = os.path.splitext(file_name)[0]
            folder_path = os.path.join(video_directory, folder_name)
            
            # Create the new folder if it does not exist
            if not os.path.exists(folder_path):
                os.mkdir(folder_path)
            
            # Move the file into the new folder
            shutil.move(os.path.join(video_directory, file_name), os.path.join(folder_path, file_name))
    
    print("Videos and their corresponding code scripts have been organized into their respective folders.")

def undo_organization(video_directory):
    # List all folders in the video directory
    folders = [f for f in os.listdir(video_directory) if os.path.isdir(os.path.join(video_directory, f))]
    
    for folder_name in folders:
        folder_path = os.path.join(video_directory, folder_name)
        files = os.listdir(folder_path)
        
        for file_name in files:
            # Move the file back to the original directory
            shutil.move(os.path.join(folder_path, file_name), os.path.join(video_directory, file_name))
        
        # Remove the folder after moving the files
        os.rmdir(folder_path)
    
    print("Undo complete. All files have been moved back to the original directory.")

def main():
    print("Choose an option to proceed:")
    print("1. Organize videos into folders")
    print("2. Organize videos and their corresponding code scripts into folders")
    print("3. Undo the last organization")

    choice = input("Enter your choice (1, 2, or 3): ")
    
    # Specify the path to your video directory
    video_directory = '/home/evans/Desktop/OMNI Research/OmniWork/Test'
    
    if choice == '1':
        organize_videos(video_directory)
    elif choice == '2':
        organize_videos_with_code(video_directory)
    elif choice == '3':
        undo_organization(video_directory)
    else:
        print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()