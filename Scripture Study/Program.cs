using System;


// Exceeded expectations by adding a word counter displaying the words that you user has remaining


class Program
{
    static void Main(string[] args)
    {

        string choice = "";

        Verse verse1 = new Verse();


        int wordCount = verse1.GetVerseCount();
        int wordsLeft = wordCount;

    
        while (choice != "quit")
        {



            Console.Clear();

            verse1.DisplayVerse();

            Console.WriteLine();
            

            
            Console.WriteLine($"(You Have {wordsLeft} words left) PRESS ENTER TO REMOVE MORE WORDS OR TYPE OUT QUIT TO END THE PROGRAM");

            choice = Console.ReadLine();

            verse1.HideRandomWords();

            if (wordsLeft <= 0) {break;}

            wordsLeft -= 3;

            if (wordsLeft < 0) {wordsLeft = 0;}

        }

    }
}