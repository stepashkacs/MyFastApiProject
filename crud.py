import asyncio

from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload, Session, selectinload

from core.models import db_helper, User, Profile, Post, Order, Product

#Запросы в базу данных
# async def create_user(session: AsyncSession, username: str) -> User:
#     user = User(username=username)
#     session.add(user)
#     await session.commit()
#     print('user', user)
#     return user
#
# async def get_user_by_username(session: AsyncSession, username: str) -> User | None:
#     stmt = select(User).where(User.username == username)
#     # result: Result = await session.execute(stmt)
#     # user: User | None = result.scalar_one_or_none()
#     user : User | None = await session.scalar(stmt)
#     print('Found user!', username, user)
#     return user
#
# async def create_user_profile(
#         session: AsyncSession,
#         user_id: int,
#         first_name: str | None = None,
#         last_name: str | None = None
# ) -> Profile:
#     profile=Profile(
#         user_id=user_id,
#         first_name=first_name,
#         last_name=last_name
#     )
#     session.add(profile)
#     await session.commit()
#     return profile
#
# async def show_users_with_profiles(session: AsyncSession) -> list[User]:
#     # stmt = select(User).options(joinedload(User.profile)).order_by(User.id)
#     stmt = select(User).options(joinedload(User.profile)).order_by(User.id)
#     # result: Result = await session.execute(stmt)
#     # users = result.scalars()
#     users = await session.scalars(stmt)
#     for user in users:
#         print(user)
#         print(user.profile.first_name)
#
#
# async def create_posts(
#     session: AsyncSession,
#     user_id: int,
#     *posts_titles: str
# ) -> list[Post]:
#     posts = [
#         Post(title=title, user_id=user_id)
#         for title in posts_titles
#     ]
#     session.add_all(posts)
#     await session.commit()
#     print(posts)
#     return posts
#
# async def get_users_with_posts(
#     session: AsyncSession,
# ):
#     # stmt = select(User).options(joinedload(User.posts)).order_by(User.id)
#     stmt = (
#         select(User)
#         .options(
#             # joinedload(User.posts),
#             selectinload(User.posts),
#         )
#         .order_by(User.id)
#     )
#     # users = await session.scalars(stmt)
#     # result: Result = await session.execute(stmt)
#     # # users = result.unique().scalars()
#     # users = result.scalars()
#     users = await session.scalars(stmt)
#
#     # for user in users.unique():  # type: User
#     for user in users:  # type: User
#         print("**" * 10)
#         print(user)
#         for post in user.posts:
#             print("-", post)
#
#
# async def get_users_with_posts_and_profiles(
#     session: AsyncSession,
# ):
#     stmt = (
#         select(User)
#         .options(
#             joinedload(User.profile),
#             selectinload(User.posts),
#         )
#         .order_by(User.id)
#     )
#     users = await session.scalars(stmt)
#
#     for user in users:  # type: User
#         print("**" * 10)
#         print(user, user.profile and user.profile.first_name)
#         for post in user.posts:
#             print("-", post)
#
#
#
# async def get_posts_with_authors(session: AsyncSession):
#     stmt = select(Post).options(joinedload(Post.user)).order_by(Post.id)
#     posts = await session.scalars(stmt)
#
#     for post in posts:
#         print('**'*10)
#         print('-post', post)
#         print('-author', post.user)
#         print('**'*10)
#
#
# async def get_profiles_with_users_and_users_with_posts(session:AsyncSession):
#     stmt = (
#         select(Profile)
#         .options(
#             joinedload(Profile.user).selectinload(User.posts),
#         )
#         .order_by(Profile.id)
#     )
#
#     profiles = await session.scalars(stmt)
#     for profile in profiles:
#         print(profile.first_name, profile.user)
#         print(profile.user.posts)
#
#
# async def main_relation(session: AsyncSession):
#     await create_user(session=session, username='john')
#     await create_user(session=session, username='sam')
#     await create_user(session=session, username='stepashka')
#     await get_user_by_username(session=session, username='sam')
#     user_stepashka = await get_user_by_username(session=session, username='stepashka')
#     user_john = await get_user_by_username(session=session, username='john')
#     user_sam = await get_user_by_username(session=session, username='sam')
#     await create_user_profile(
#         session=session,
#         user_id=user_john.id,
#         first_name='John'
#     )
#     await create_user_profile(
#         session=session,
#         user_id=user_sam.id,
#         first_name='Sam',
#         last_name='White'
#     )
#     await show_users_with_profiles(session=session)
#     await create_posts(
#         session,
#         user_john.id,
#         "sql",
#         "fastapi"
#     )
#     await create_posts(
#         session,
#         user_sam.id,
#         "Fastapi introduction",
#         "Django introduction"
#     )
#
#     await get_users_with_posts(session=session)
#     await get_posts_with_authors(session=session)
#     await get_users_with_posts_and_profiles(session=session)
#     await get_profiles_with_users_and_users_with_posts(session=session)


async def crete_order(
        session: AsyncSession,
        promocode: str | None = None,
) -> Order:
    order = Order(promocode=promocode)
    session.add(order)
    await session.commit()
    return order


async def create_product(
    session: AsyncSession,
    name: str,
    description: str,
    price: int,
) -> Product:
    product = Product(
        name=name,
        description=description,
        price=price
    )
    session.add(product)
    await session.commit()
    return product



async def demo_m2m(session: AsyncSession):
    order_one = await crete_order(session=session)
    order_promo = await crete_order(session=session, promocode="promocode")

    monitor = await create_product(
        session=session,
        name = 'BENQ ZOWIE 2540K',
        description = '240 HZ gaming monitor',
        price = 500
    )

    macbook = await create_product(
        session=session,
        name = 'MacBook Pro M3 Max',
        description = 'Most expensiv notebook',
        price = 3000
    )

    mouse = await create_product(
        session=session,
        name='Logitech G305',
        description = 'Good mouse',
        price = 50
    )

    order_one = await session.scalar(
        select(Order)
        .where(Order.id == order_one.id)
        .options(
            selectinload(Order.products),
        ),
    )
    order_promo = await session.scalar(
        select(Order)
        .where(Order.id == order_promo.id)
        .options(
            selectinload(Order.products),
        ),
    )

    order_one.products.append(monitor)
    order_one.products.append(macbook)
    order_promo.products.append(macbook)
    order_promo.products.append(mouse)

    await session.commit()

async def main():
    async with db_helper.session_factory() as session:
        # await main_relation(session=session)
        await demo_m2m(session=session)





if __name__ == '__main__':
    asyncio.run(main())