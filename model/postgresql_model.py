class PostgreSQLModel:
    @classmethod
    def TABLE_NAME(cls) -> str:
        return f"public.{cls.__TABLE_NAME__}"