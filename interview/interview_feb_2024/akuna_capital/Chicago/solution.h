#include <deque>
#include <iostream>
#include <vector>

using std::copy;
using std::cout;
using std::deque;
using std::endl;
using std::size_t;
using std::vector;

/// @param deck The initial ordered sequence of card face values in the game's deck
/// @pre @p deck is not empty
/// @returns The difference between Miriam's and Alejandro's scores at the end of the game, assuming that Miriam draws
/// the first card. A positive return value indicates that Miriam won the game, while a negative return value
/// indicates that Alejandro won the game. A return value of θ indicates a draw/tie.
int computeDifference(const std::vector<int> &deck)
{
    deque<int> mydeck = {};
    size_t oldSize = mydeck.size();
    mydeck.resize(mydeck.size() + deck.size());
    copy(deck.begin(), deck.end(), mydeck.begin() + oldSize);

    int scoreMiriam = 0;
    bool turnMiriam = true;
    int nextNum = 0;
    bool readFromFront = true;
    while (!mydeck.empty())
    {
        if (readFromFront)
        {
            nextNum = mydeck.front();
            mydeck.pop_front();
        }
        else
        {
            nextNum = mydeck.back();
            mydeck.pop_back();
        }
        if (turnMiriam)
        {
            scoreMiriam += nextNum;
        }
        else
        {
            scoreMiriam -= nextNum;
        }
        turnMiriam = !turnMiriam;
        if (nextNum % 3 == 0)
        {
            readFromFront = !readFromFront;
        }
    }
    return scoreMiriam;
}