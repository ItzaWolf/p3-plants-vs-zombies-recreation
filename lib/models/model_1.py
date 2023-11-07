# from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
# from sqlalchemy.orm import Session, declarative_base

# Base = declarative_base()

# class Users(Base):
#     __tablename__ = "Users"
#     id = Column(Integer, primary_key= True)
#     username = Column(String, nullable=False)
#     password = Column(String, nullable=False)

# class Scores(Base):
#     __tablename__ = "Scores"
#     id = Column(Integer, primary_key= True)
#     user_id = Column(Integer, ForeignKey("Users.id"))
#     score = Column(Integer, nullable=False)

# if __name__ == "__main__":
#     engine = create_engine("sqlite:///pvz.db")
#     # Users.__table__.drop(engine)
#     # Scores.__table__.drop(engine)
#     Base.metadata.create_all(engine)
#     with Session(engine) as session:
#         '''
#         The session object will allow use to perform CRUD on our models
#         Session.add()
#         Session.add_all([])
#         Session.query()
#             .all()
#             .orderby() ex: Table.name.desc()
#             .limit() ex: limit(2)
#             .filter() ex Table.name = "name"
#             .update() ex {Table.name: newname}
#         Session.delete()
#         Session.commit()
#         '''

#         all_users = session.query(Users).order_by(Users.username.asc()).all()

#         search_users = input("Enter a username: ")

#         search = session.query(Users).filter(Users.username == search_users).first()

#         if search:
#             print("User Exists")
#             session.delete(search)
#             session.commit()
#         else:
#             print("No user found")

#         new_user = input("Enter a Username: ")
#         new_password = input("Enter a Password: ")
#         n_user = Users(username = new_user, password = new_password)
#         session.add(n_user)
#         session.commit()
#         new_score = input("Enter a Score: ")
#         n_score = Scores(user_id = n_user.id, score = new_score)
#         session.add(n_score)
#         session.commit()
