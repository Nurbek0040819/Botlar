from aiogram.fsm.state import State, StatesGroup


class CategoryStates(StatesGroup):
    addCategoryState = State()

    startEditCategoryState = State()
    finishEditCategoryState = State()

    startDeleteCategoryState = State()
    finishDeleteCategoryState = State()


class ProductStates(StatesGroup):
    add_SelectCategoryProdState = State()
    add_TitleCategoryProdState = State()
    add_TextCategoryProdState = State()
    add_ImageCategoryProdState = State()
    add_PriceCategoryProdState = State()
    add_PhoneCategoryProdState = State()

    edit_SelectCategoryProdState = State()
    edit_TitleCategoryProdState = State()
    edit_TextCategoryProdState = State()
    edit_ImageCategoryProdState = State()
    edit_PriceCategoryProdState = State()
    edit_PhoneCategoryProdState = State()



