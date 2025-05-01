#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

int main(){
    int m;
    cin >> m;
    vector<double> streams = {0.0};
    for (int i = 0; i < m; i++){
        double stream;
        cin >> stream;
        streams.push_back(stream);
    }
    
    while (true){
        int split;
        cin >> split;

        if (split == 77){
            streams.erase(streams.begin());
            for (double i:streams){
                cout << round(i) << " ";
            }
            return 0;
        }
        if (split == 99){
            int pos, flow;
            cin >> pos >> flow;
            double lstream = streams[pos] * (flow/100.0);
            double rstream = streams[pos] * ((100-flow)/100.0);
            streams.erase(streams.begin()+pos);
            streams.insert(streams.begin()+pos, rstream);
            streams.insert(streams.begin()+pos,lstream);

        }
        else{
            int pos;
            cin >> pos;
            double lstream = streams[pos];
            double rstream = streams[pos+1];
            streams.erase(streams.begin() + pos);
            streams.erase(streams.begin() + pos);
            streams.insert(streams.begin() + pos,lstream+rstream);
        }
    }
    
    return 0;
}