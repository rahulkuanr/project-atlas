from sqlalchemy import select

from app.core.database import SessionLocal
from app.models.customer import Customer


def test_create_and_read_customer():
    with SessionLocal() as session:
        customer = Customer(
            name="Test Customer",
            email="test@example.com",
        )

        session.add(customer)
        session.commit()
        session.refresh(customer)

        assert customer.id is not None
        assert customer.name == "Test Customer"
        assert customer.email == "test@example.com"

        result = session.scalar(select(Customer).where(Customer.id == customer.id))

        assert result is not None
        assert result.name == "Test Customer"
        assert result.email == "test@example.com"

        session.delete(customer)
        session.commit()
