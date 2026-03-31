
class Verse
{
    Reference ref1 = new Reference("2 Nephi", 31, 20);

    private string _verseToMemorize = "Wherefore, ye must press forward with a steadfastness in Christ, having a perfect brightness of hope, and a love of God and of all men. Wherefore, if ye shall press forward, feasting upon the word of Christ, and endure to the end, behold, thus saith the Father: Ye shall have eternal life.";

    private List<Word> _words;

    public Verse()
    {
        TurnListIntoObects();  
    }

    public int GetVerseCount()
    {
        return _words.Count();
    }

    public void TurnListIntoObects()
    {
        string[] splitWords = _verseToMemorize.Split(' ');
        _words = new List<Word>();

        foreach (string wordText in splitWords)
        {
            Word word = new Word(wordText);
            _words.Add(word);
        }
    }

    public void DisplayVerse()
    {
        Console.Write(ref1.MakeReference());

        foreach (Word word in _words)
        {
            Console.Write(word.GetDisplayText() + " ");
        }

        Console.WriteLine();
    }

    public void HideRandomWords()
{

    Random random = new Random();
    int hiddenCount = 0;

    while (hiddenCount < 3)
    {
        int index = random.Next(_words.Count);
        Word word = _words[index];

        if (!word.IsHidden)
        {
            word.Hide();
            hiddenCount++;
        }

        if (_words.TrueForAll(w => w.IsHidden))
            break;
    }
}

    public bool AreAllWordsHidden()
    {
        return _words.TrueForAll(w => w.IsHidden);
    }

}
