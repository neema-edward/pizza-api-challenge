from server.app import create_app, db
from server.models.restaurant import Restaurant
from server.models.pizza import Pizza
from server.models.restaurant_pizza import RestaurantPizza

def seed_data():
    app = create_app()
    with app.app_context():
        db.drop_all()
        db.create_all()
        
        # Seed restaurants
        r1 = Restaurant(name="Neema's Pizza", address="27 Main St")
        r2 = Restaurant(name="Pizza Palace", address="456 Kenyatta Ave")
        db.session.add_all([r1, r2])
        
        # Seed pizzas
        p1 = Pizza(name="Margherita", ingredients="Dough, Tomato Sauce, Cheese")
        p2 = Pizza(name="Pepperoni", ingredients="Dough, Tomato Sauce, Cheese, Pepperoni")
        db.session.add_all([p1, p2])
        
        db.session.commit()
        
        # Seed restaurant_pizzas
        rp1 = RestaurantPizza(price=10, restaurant_id=r1.id, pizza_id=p1.id)
        rp2 = RestaurantPizza(price=12, restaurant_id=r2.id, pizza_id=p2.id)
        db.session.add_all([rp1, rp2])
        
        db.session.commit()

if __name__ == '__main__':
    seed_data()