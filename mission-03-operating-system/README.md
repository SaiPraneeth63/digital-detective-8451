# Mission 3 - Understand the operating system

## 1. Task/objective
Explore the operating system, running processes, storage, absolute/relative paths, and file permissions, and describe the core responsibilities of an operating system .

## 2. Work completed
- Explored macOS environment details, active account identity, and available disk storage using Terminal commands (`sw_vers`, `whoami`, `df -h`).
- Observed running system processes and understood Process Identifiers (PIDs) using `ps aux`.
- Reviewed absolute and relative paths along with file permission bits (`rwx`).
- Completed the operating system responsibilities breakdown table.

## 3. Commands / tools used
- `sw_vers`: Displays operating system version information.
- `whoami`: Displays the currently active user account name.
- `df -h`: Reports disk space usage in a human-readable format.
- `ps aux`: Displays a snapshot of currently running processes.
- `ls -l`: Displays detailed file listings including permissions.

## 4. My understanding
The operating system acts as an intermediary between physical hardware and user applications. It manages system resources, schedules processes via unique PIDs, controls file access through permission attributes (`rwx`), and maintains directory structures using absolute and relative paths.

## 5. Difficulties faced
No major difficulties.

## 6. How I resolved them
Not applicable.

## 7. Evidence / files
### Task 3.4: Operating-System Responsibilities
| OS responsibility | Your explanation | Example |
| :--- | :--- | :--- |
| Process management | Allocates CPU time and resources to start, run, and stop programs. | Launching VS Code or Terminal. |
| Memory management | Tracks system RAM usage, assigning and freeing memory space for active apps. | Allocating RAM when opening multiple browser tabs. |
| Device management | Communicates with hardware peripherals using device drivers. | Sending print jobs to a connected printer. |
| File management | Organizes, reads, writes, and secures files and folders on storage drives. | Saving or opening files in a text editor. |
| User interface / shell | Provides a graphical or command-line way for users to interact with the system. | Using the macOS desktop or Terminal. |
| Security and permissions | Controls access to system files, resources, and user accounts using credentials and permissions. | Restricting file modification rights to authorized owners. |

## 8. Commit details
- Commit message: "Document operating system and file management"
- Pushed successfully to GitHub.