#include <iostream>
using namespace std;

struct Node {
    int data;
    Node* prev;
    Node* next;
};

Node* insert(Node* head, int data) {
    Node* newNode = new Node();
    newNode->data = data;
    newNode->prev = NULL;
    newNode->next = NULL;

    if (head == NULL) return newNode;

    Node* temp = head;
    while (temp->next != NULL)
        temp = temp->next;

    temp->next = newNode;
    newNode->prev = temp;

    return head;
}

Node* rotateClockwise(Node* head, int k) {
    if (head == NULL || k == 0) return head;

    Node* temp = head;
    int count = 1;

    while (temp->next != NULL) {
        temp = temp->next;
        count++;
    }

    Node* tail = temp;
    k = k % count;
    if (k == 0) return head;

    int steps = count - k;
    temp = head;

    for (int i = 1; i < steps; i++)
        temp = temp->next;

    Node* newHead = temp->next;
    temp->next = NULL;
    newHead->prev = NULL;

    tail->next = head;
    head->prev = tail;

    return newHead;
}

void display(Node* head) {
    Node* temp = head;
    while (temp != NULL) {
        cout << temp->data;
        if (temp->next != NULL) cout << " ";
        temp = temp->next;
    }
}

int main() {
    int n;
    cin >> n;

    Node* head = NULL;

    for (int i = 0; i < n; i++) {
        int x;
        cin >> x;
        head = insert(head, x);
    }

    int k;
    cin >> k;

    head = rotateClockwise(head, k);
    display(head);

    return 0;
}