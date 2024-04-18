class Solution {
public:
    string simplifyPath(string path) {
        stack<string>st;
        string temp = "";
        vector<string> ans;
        
        for(int i = 0; i < path.size(); i++){
            temp += path[i];
            if(path[i] == '/')
                temp.pop_back();
            else if(i != path.size()-1)
                continue;
            
            if(st.size()>0 &&  temp == ".." )
                st.pop();

            else if(temp.size()>0 && temp != "." && temp != ".." )
                st.push(temp);
                temp = "";
        }
        
        if(st.size() == 0) 
            return "/";
        
        while(st.size() > 0) {
          ans.push_back(st.top());
          ans.push_back("/");
          st.pop();
        }

      reverse(ans.begin(),ans.end());

      for(auto i : ans) 
          temp+=i;
      return temp;
    }
};
