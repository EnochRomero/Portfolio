// I exceeded expectations by addressing an additional journaling issue. 
// One common issue of looking back on the past is that people 
// (especially those dealing with some kind of depression) tend to think of their 
// lives as more sad looking back when compared to how they actually felt in the moment, 
// so I added a mood tracker into the program. This will help people more accurately see 
// and remember the good days they have had.



using Develop02;

class Program
{

        static void DisplayMenu()
    {
        Console.WriteLine("Please Select One of the Following Choices:");
        Console.WriteLine("1. Write");
        Console.WriteLine("2. Display");
        Console.WriteLine("3. Load");
        Console.WriteLine("4. Save");
        Console.WriteLine("5. Quit");
        
    }


    static void Main(string[] args)
    {
        Journal journal = new Journal();
        string choice = "0";

        while (choice != "5")
        {
            DisplayMenu();
            choice = Console.ReadLine();

            // WRITE
            if (choice == "1")
            {
                UserEntry newEntry = new UserEntry();
                Console.WriteLine(newEntry.GivenPrompt);
                newEntry.UserTextEntry = Console.ReadLine();

                Console.WriteLine("On a scale from 1-10, how happy are you today?");
                newEntry.UserMood = Console.ReadLine();

                journal.AddEntry(newEntry);
            }




            // DISPLAY
            else if (choice == "2")
            {
                foreach (UserEntry entry in journal.Entries)
                {
                    Console.WriteLine();
                    Console.WriteLine(entry.MakeEntry());
                    Console.WriteLine();
                    Console.WriteLine("======================================");
                }
            }

            // LOAD
            else if (choice == "3")
            {
                Console.Write("Enter the file name to load: ");
                string fileName = Console.ReadLine();

                if (File.Exists(fileName))
                {
                    journal.LoadEntries(fileName);
                    Console.WriteLine("Entries loaded successfully.");
                }
                else
                {
                    Console.WriteLine("File not found.");
                }
            }



            // SAVE
            else if (choice == "4")
            {
                Console.Write("Enter a name for the save file: ");
                string fileName = Console.ReadLine();
                journal.SaveEntries(fileName);
                Console.WriteLine("Entries saved successfully.");
            }



        }
    }

}