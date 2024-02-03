#include <cctype>
#include <iostream>
#include <string>
#include <utility>
#include <vector>
#include <stack>

using std::atoi;
using std::cout;
using std::endl;
using std::make_pair;
using std::pair;
using std::string;
using std::vector;

class Solution
{
public:
    std::string decodeString(const std::string &s)
    {
        std::stack<std::pair<int, std::string>> stack;
        std::string current = "";
        int count = 0;

        for (char item : s)
        {
            if (isdigit(item))
            {
                count = count * 10 + (item - '0');
            }
            else if (item == '[')
            {
                stack.push({count, current});
                current = "";
                count = 0;
            }
            else if (item == ']')
            {
                auto last = stack.top();
                stack.pop();
                string temp = "";
                for (int j = 0; j < last.first; ++j) {
                    temp.append(current);
                }
                current = last.second + temp;
            }
            else
            {
                current += item;
            }
        }

        return current;
    }
};

int main()
{
    Solution s = Solution();
    cout << s.decodeString("2[abc]3[cd]ef") << endl;
}
