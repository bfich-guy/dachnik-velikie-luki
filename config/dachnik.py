from enum import Enum


class ProductTypes(Enum):
    JAR_REGULAR = "jar_regular"
    JAR_SCREW = "jar_screw"

    LID_REGULAR = "lid_regular"
    LID_SCREW = "lid_screw"

    SEAMINGMACHINE_AUTO = "seamingmachine_auto"
    SEAMINGMACHINE_SEMIAUTO = "seamingmachine_semiauto"
    SEAMINGMACHINE_SPIRAL = "seamingmachine_spiral"


class ProductNames(Enum):
    JAR_REGULAR = "Стеклянная банка СКО"
    JAR_SCREW = "Стеклянная банка ТО"

    LID_REGULAR = "Крышка СКО"
    LID_SCREW = "Крышка ТО"

    SEAMINGMACHINE_AUTO = "Закаточная машинка автомат"
    SEAMINGMACHINE_SEMIAUTO = "Закаточная машинка полуавтомат"
    SEAMINGMACHINE_SPIRAL = "Закаточная машинка ручная"


class ProductExtraDataKeys(Enum):
    AMOUNT = "amount"
    DIAMETER = "diameter"
    VOLUME = "volume"


class DachnikPhrases(Enum):
    UNKNOWN_PRODUCT_TYPE = "Ой-ё... А такого товара нет у меня в ларьке. Что же делать... Ладно, в следующий раз он появится, приходите еще! Было приятно поразмять кости."
    UNKNOWN_PRODUCT_DESCRIPTION = "Воу, этот товар - что-то новнькое!"

    SEARCHED_PRODUCT = ("Я обыскал каждую полочку моего славного ларька в поисках товара под названием ", " и нашел ", " штук такого добра.")


class MeasurementUnits(Enum):
    AMOUNT = "шт."

    LITER = "л."
    MILLIMETER = "мм."


class ConversionFactors(Enum):
    MILLILITER_TO_LITER = 1000


product_type_map: dict[str, str] = {
    ProductTypes.JAR_REGULAR.value: ProductNames.JAR_REGULAR.value,
    ProductTypes.JAR_SCREW.value: ProductNames.JAR_SCREW.value,

    ProductTypes.LID_REGULAR.value: ProductNames.LID_REGULAR.value,
    ProductTypes.LID_SCREW.value: ProductNames.LID_SCREW.value,

    ProductTypes.SEAMINGMACHINE_AUTO.value: ProductNames.SEAMINGMACHINE_AUTO.value,
    ProductTypes.SEAMINGMACHINE_SEMIAUTO.value: ProductNames.SEAMINGMACHINE_SEMIAUTO.value,
    ProductTypes.SEAMINGMACHINE_SPIRAL.value: ProductNames.SEAMINGMACHINE_SPIRAL.value,
}

