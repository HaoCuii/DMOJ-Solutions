    /*
    HARDEST QUESTION OAT. how the FUCK IS IT A 10 POINTER

    Easy version of question first (pretend that they don't have ranges)
    Observe that the optimal point is always the optimal point between the two people that take the LONGEST to complete.
    For example if the optimal point between 1,2 takes 2 seconds, 2,3 takes 1 seconds, and 1,3 takes 4 seconds. We know that the optimal point is just the optimal meeting point between person 1 and 3
    ^^^^ (the proof for this is left as an excercise to the reader)

    now we can generalize the problem to: choose any 2 people in the set of people so the time is maximized. 
    First sort by position.
    Then this can be achieved using brute force n choose 2 operations which is o(n^2). This is too slow so how can we achieve in subquadratic time?
    Notice how the time can be calculated as (Xj - Xi) / (Vi + Vj) between point j and i where j > i.
    we can binary search for the largest value of t. First set t to an arbitrary value.
    if t <= (Xj - Xi) / (Vi + Vj) then we can increase out t, otherwise we will decrease our t until we narrow in on one t.
    Finding binary searching will take logn operations, so to get subquadratic time, for each iteration in the binary search, we musst see if the inequality is satisfied in o(n) time.
    How tf will we do this? isn't that the same as before?

    By manipulating our inequality into -> Xi + t * Vi <= Xj - t * Vj we can see that our original inequality will hold true if for a point J, there is a point (I) before it that is smaller.
    By maintaining the smallest value before J and looping through the list, we can do this in one loop.

    We've solved the easier version. Now adding back ranges is ez.
    We just set Xi as Xi + Di and Xj as Xj - Dj.
    Thus we can find the optimal point in O(N * 60)???.
    */

    #include <bits/stdc++.h>
    using namespace std;

    using ll = long long;
    struct Person {
        ll p, w, d;
        bool operator<(const Person& o) const { return p < o.p; }
    };

    int n;
    vector<Person> friends(n);


    vector<ll> check(long double t){ //returns a boolean if inequality is true, then the left and right index where it's true. 
        long double minleft = LLONG_MAX;
        ll minleft_idx = -1;
        for (int i = 0; i < n; i++){
            if ((friends[i].p - friends[i].d) - t * friends[i].w  >= minleft){
                return {1, minleft_idx, i};
            }
            else if ((friends[i].p + friends[i].d) + t * friends[i].w < minleft){
                minleft = (friends[i].p + friends[i].d) + t * friends[i].w;
                minleft_idx = i;
            }
        }
        return {0, -1,-1};    
    }

    int main() {
        ios::sync_with_stdio(false);
        cin.tie(nullptr);
        cin >> n; 
        friends.resize(n);
        ll temp = LLONG_MAX;
        for (int i = 0; i < n; i++) {
            cin >> friends[i].p >> friends[i].w >> friends[i].d;
            temp = min(temp, friends[i].w);
        }

        sort(friends.begin(),friends.end());
        long double lo = 0;
        long double hi = ((long double)friends[n-1].p - (long double)friends[0].p) / (2.0L * (long double)temp); //find a large hi that's not absurd

        for (int it = 0; it < 200; it ++){
            long double mid = (lo + hi)/2;
            if (check(mid)[0]){
                hi = mid;
            }
            else{
                lo = mid;
            }
        }
    }
