/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
#include <iostream>
#include <memory>
#include <string>
#include <vector>
using std::cout;
using std::endl;
using std::string;

struct ListNode
{
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
    void print()
    {
        ListNode *node = this;
        while (node)
        {
            cout << node->val;
            if (!node->next)
            {
                cout << endl;
            }
            else
            {
                cout << " ";
            }
            node = node->next;
        }
    }
};

ListNode *push(ListNode *node, int val)
{
    ListNode *nextNode = new ListNode(val);
    node->next = nextNode;
    return node->next;
}

class Solution
{
public:
    ListNode *reverseList(ListNode *head)
    {
        ListNode *pre_node = nullptr;
        ListNode *next_node = nullptr;
        ListNode *cur = head;
        while (cur)
        {
            cout << cur->val << endl;
            next_node = cur->next;
            cur->next = pre_node;
            pre_node = cur;
            cur = next_node;
        }
        return pre_node;
    }

    int pairSum(ListNode *head)
    {
        std::vector<int> vec = {};
        ListNode *cur = head;
        while (cur) {
            vec.emplace_back(cur->val);
            cur = cur->next;
        }
        int max_sofar = 0;
        int length = vec.size();
        if (length == 0) {
            return max_sofar;
        }
        int temp = 0;
        for (int i = 0; i < length; ++i) {
            temp = vec[i] + vec[length - 1 - i];
            if (temp > max_sofar) {
                max_sofar = temp;
            }
        }
        return max_sofar;
    }
};

int main(int argc, char const *argv[])
{
    int arr[5] = {1, 2, 3, 4, 5};
    ListNode fakehead = ListNode(0);
    ListNode *cur = &fakehead;
    for (auto val : arr)
    {
        cur = push(cur, val);
    }
    fakehead.print();
    ::Solution s = Solution();
    fakehead.next = s.reverseList(fakehead.next);
    fakehead.next->print();
    return 0;
}
