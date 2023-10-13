use std::collections::BinaryHeap;
use std::cmp::Ordering;
use std::cmp::Reverse;

#[derive(Debug, PartialEq, Eq, Clone)]
struct Order {
    price: i32,
    quantity: i32,
    id: i32,
}

impl Ord for Order {
    fn cmp(&self, other: &Self) -> Ordering {
        self.price.cmp(&other.price)
    }
}

impl PartialOrd for Order {
    fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
        Some(self.cmp(other))
    }
}

struct MarketMaker {
    bid: BinaryHeap<Reverse<Order>>,  // Min heap for bids
    ask: BinaryHeap<Order>,           // Max heap for asks
}

impl MarketMaker {
    pub fn new() -> Self {
        MarketMaker {
            bid: BinaryHeap::new(),
            ask: BinaryHeap::new(),
        }
    }

    pub fn insert(&mut self, values: [i32; 4]) {
        let order = Order {
            price: values[1],
            quantity: values[2],
            id: values[3],
        };

        match values[0] {
            0 => self.bid.push(Reverse(order)),
            1 => self.ask.push(order),
            _ => panic!("Invalid type"),
        }

        self.evaluate()
    }

    fn evaluate(&mut self) {
        let mut total_traded = 0;
        let mut parties_involved = vec![];

        while let Some(Reverse(bid_order)) = self.bid.peek().cloned() {
            if let Some(ask_order) = self.ask.peek().cloned() {
                if bid_order.price >= ask_order.price {
                    // Trade possible
                    let trade_qty = bid_order.quantity.min(ask_order.quantity);
                    total_traded += trade_qty;

                    parties_involved.push(bid_order.id);
                    parties_involved.push(ask_order.id);

                    if bid_order.quantity > ask_order.quantity {
                        let mut top_bid = self.bid.pop().unwrap().0;
                        top_bid.quantity -= trade_qty;
                        self.bid.push(Reverse(top_bid));
                        self.ask.pop();
                    } else {
                        let mut top_ask = self.ask.pop().unwrap();
                        top_ask.quantity -= trade_qty;
                        self.ask.push(top_ask);
                        self.bid.pop();
                    }
                } else {
                    break;
                }
            } else {
                break;
            }
        }

        if total_traded > 0 {
            println!("Quantity traded: {}", total_traded);
            println!("Parties involved: {:?}", parties_involved);
        } else {
            println!("No new transactions");
        }
    }
}

fn main() {
    let mut mm = MarketMaker::new();

    mm.insert([0, 100, 5, 1]);
    mm.insert([1, 90, 3, 2]);
    mm.insert([1, 95, 2, 3]);
}
