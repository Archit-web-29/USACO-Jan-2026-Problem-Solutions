#include <iostream>
#include <algorithm>

using namespace std;

typedef long long ll;

ll solve_type1(ll c, ll T) {
    ll cur_p = c;
    ll cur_t = c;
    
    while (cur_t < T) {
        ll next_t = cur_t + 1;
        ll limit = next_t / 2;

        if (cur_p > limit) {
            ll next_interaction = 2 * cur_p;
            
            // If the next interaction is beyond T, we are done.
            if (next_interaction > T) return cur_p;


            cur_t = next_interaction - 1;
        } else {
            ll steps_to_zero = cur_p;
            ll time_remaining = T - cur_t;
            
            ll can_step = min(steps_to_zero, time_remaining);
            
            cur_p -= can_step;
            cur_t += can_step;
            
            if (cur_p == 0 && cur_t < T) {
                cur_t++;
                cur_p = cur_t / 2;
            }
        }
    }
    return cur_p;
}

ll solve_type2(ll x, ll t) {
    while (t > 0) {
        if (x > t / 2) {
            return x; 
        }
        
        if (x == t / 2) {
            x = 0;
            t--;
        } else {
            ll k = (t - 2 * x) / 3;
            if (k == 0) {
                x++;
                t--;
            } else {
                x += k;
                t -= k;
            }
        }
        
        if (x >= t) return x; 
    }
    return 0;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int Q;
    if (cin >> Q) {
        while (Q--) {
            int type;
            ll a, b;
            cin >> type >> a >> b;
            if (type == 1) {
                cout << solve_type1(a, b) << "\n";
            } else {
                cout << solve_type2(a, b) << "\n";
            }
        }
    }
    return 0;
}