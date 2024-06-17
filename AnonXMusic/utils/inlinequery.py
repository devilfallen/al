from pyrogram.types import InlineQueryResultArticle, InputTextMessageContent

answer = []

answer.extend(
    [
        InlineQueryResultArticle(
            title="Pᴀᴜsᴇ",
            description=f"Görüntülü sohbette geçerli yayın duraklatıldı 😒.",
            thumb_url="https://te.legra.ph/Alem-Music-05-27",
            input_message_content=InputTextMessageContent("/pause"),
        ),
        InlineQueryResultArticle(
            title="Rᴇsᴜᴍᴇ",
            description=f"Görüntülü sohbette geçerli yayın devam ettirildi 🥰.",
            thumb_url="https://te.legra.ph/Alem-Music-05-27",
            input_message_content=InputTextMessageContent("/resume"),
        ),
        InlineQueryResultArticle(
            title="Sᴋɪᴩ",
            description=f"Sıradaki parça oynatılıyor 🥳.",
            thumb_url="https://te.legra.ph/Alem-Music-05-27",
            input_message_content=InputTextMessageContent("/skip"),
        ),
        InlineQueryResultArticle(
            title="Eɴᴅ",
            description="Alem Müzik Yayını Sonlandırıldı 🥺.",
            thumb_url="https://te.legra.ph/Alem-Music-05-27",
            input_message_content=InputTextMessageContent("/end"),
        ),
        InlineQueryResultArticle(
            title="Sʜᴜғғʟᴇ",
            description="Parça Listesi Karıştırıldı 🧐.",
            thumb_url="https://te.legra.ph/Alem-Music-05-27",
            input_message_content=InputTextMessageContent("/shuffle"),
        ),
        InlineQueryResultArticle(
            title="Lᴏᴏᴩ",
            description="Oynatılan parça görüntülü sohbette döngüye alındı 😵‍💫.",
            thumb_url="https://te.legra.ph/Alem-Music-05-27",
            input_message_content=InputTextMessageContent("/loop 3"),
        ),
    ]
)
