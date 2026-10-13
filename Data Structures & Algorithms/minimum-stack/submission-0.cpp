class MinStack {
public:
    stack<int> stk; 
    MinStack() {
        
    }
    
    void push(int val) {
        stk.push(val);
    }
    
    void pop() {
        stk.pop(); 
    }
    
    int top() {
       return stk.top();
    }
    
    int getMin() {
        stack<int> cp = stk; 
        int min = cp.top(); 
        while (!cp.empty()) {
            if (cp.top() <= min) {
                min = cp.top(); 
                cp.pop(); 
            }
            else cp.pop();
        }
        return min; 
    }
};
