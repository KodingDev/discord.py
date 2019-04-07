import asyncio
import aiohttp

from .file import File
from .types import (
    RawChannelDict, RawMessageDict, RawUserDict, RawApplicationInfoDict, RawGuildMemberDict, RawRoleDict, RawInviteDict,
    RawInviteMetaDict, RawWebhookDict, RawGuildDict, RawGuildBanDict, RawGuildPruneDict, RawEmojiDict, RawAuditLogDict,
    RawCurrentUserGuildDict, RawWidgetDict, RawClientUserDict
)

from typing import Any, Optional, Union, Coroutine, List, Dict, Tuple, ClassVar, BinaryIO, Iterable
from mypy_extensions import TypedDict

class _PositionDict(TypedDict):
    id: int
    position: int

class _OverwriteDict(TypedDict):
    id: int
    type: str
    allow: int
    deny: int

async def json_or_text(response: Any) -> Any: ...

class Route:
    BASE: ClassVar[str]
    channel_id: Optional[int]
    guild_id: Optional[int]

    def __init__(self, method: str, path: str, **parameters: Any) -> None: ...

    @property
    def bucket(self) -> str: ...

class MaybeUnlock:
    def __init__(self, lock: asyncio.Lock) -> None: ...

    def __enter__(self) -> MaybeUnlock: ...

    def defer(self) -> None: ...

    def __exit__(self, type: Any, value: Any, traceback: Any) -> None: ...

class HTTPClient:
    SUCCESS_LOG: ClassVar[str]
    REQUEST_LOG: ClassVar[str]

    loop: asyncio.AbstractEventLoop
    connector: Optional[aiohttp.BaseConnector]
    token: Optional[str]
    bot_token: bool
    proxy: Optional[str]
    proxy_auth: Optional[aiohttp.BasicAuth]
    user_agent: str

    def recreate(self) -> None: ...

    async def request(self, route: Route, *, files: Optional[Iterable[File]] = ...,
                      header_bypass_delay: Optional[Union[int, float]] = ..., **kwargs: Any) -> Any: ...

    async def get_from_cdn(self, url: str) -> bytes: ...

    async def close(self) -> None: ...

    async def static_login(self, token: str, *, bot: bool) -> Any: ...

    def logout(self) -> Coroutine[Any, Any, Any]: ...

    def start_group(self, user_id: int, recipients: List[Any]) -> Coroutine[Any, Any, RawChannelDict]: ...

    def leave_group(self, channel_id: int) -> Coroutine[Any, Any, RawChannelDict]: ...

    def add_group_recipient(self, channel_id: int, user_id: int) -> Coroutine[Any, Any, Any]: ...

    def remove_group_recipient(self, channel_id: int, user_id: int) -> Coroutine[Any, Any, None]: ...

    def edit_group(self, channel_id: int, **options: Any) -> Coroutine[Any, Any, RawChannelDict]: ...

    def convert_group(self, channel_id: int) -> Coroutine[Any, Any, Any]: ...

    def start_private_message(self, user_id: int) -> Coroutine[Any, Any, RawChannelDict]: ...

    def send_message(self, channel_id: int, content: str, *, tts: bool = ..., embed: Optional[Dict[str, Any]] = ..., nonce: Optional[int] = ...) -> Coroutine[Any, Any, RawMessageDict]: ...

    def send_typing(self, channel_id: int) -> Coroutine[Any, Any, None]: ...

    def send_files(self, channel_id: int, *, files: List[Tuple[BinaryIO, str]], content: Optional[str] = ...,
                   tts: bool = ..., embed: Optional[Dict[str, Any]] = ...,
                   nonce: Optional[int] = ...) -> Coroutine[Any, Any, RawMessageDict]: ...

    async def ack_message(self, channel_id: int, message_id: int) -> None: ...

    def ack_guild(self, guild_id: int) -> Coroutine[Any, Any, Any]: ...

    def delete_message(self, channel_id: int, message_id: int, *, reason: Optional[str] = ...) -> Coroutine[Any, Any, None]: ...

    def delete_messages(self, channel_id: int, message_ids: List[int], *, reason: Optional[str] = ...) -> Coroutine[Any, Any, None]: ...

    def edit_message(self, message_id: int, channel_id: int, **fields: Any) -> Coroutine[Any, Any, RawMessageDict]: ...

    def add_reaction(self, message_id: int, channel_id: int, emoji: str) -> Coroutine[Any, Any, None]: ...

    def remove_reaction(self, message_id: int, channel_id: int, emoji: str, member_id: int) -> Coroutine[Any, Any, None]: ...

    def remove_own_reaction(self, message_id: int, channel_id: int, emoji: str) -> Coroutine[Any, Any, None]: ...

    def get_reaction_users(self, message_id: int, channel_id: int, emoji: str, limit: int, after: Optional[int] = ...) -> Coroutine[Any, Any, RawUserDict]: ...

    def clear_reactions(self, message_id: int, channel_id: int) -> Coroutine[Any, Any, None]: ...

    def get_message(self, channel_id: int, message_id: int) -> Coroutine[Any, Any, RawMessageDict]: ...

    def logs_from(self, channel_id: int, limit: int, before: Optional[int] = ..., after: Optional[int] = ..., around: Optional[int] = ...) -> Coroutine[Any, Any, List[RawMessageDict]]: ...

    def pin_message(self, channel_id: int, message_id: int) -> Coroutine[Any, Any, None]: ...

    def unpin_message(self, channel_id: int, message_id: int) -> Coroutine[Any, Any, None]: ...

    def pins_from(self, channel_id: int) -> Coroutine[Any, Any, List[RawMessageDict]]: ...

    def kick(self, user_id: int, guild_id: int, reason: Optional[str] = ...) -> Coroutine[Any, Any, None]: ...

    def ban(self, user_id: int, guild_id: int, delete_message_days: int = ..., reason: Optional[str] = ...) -> Coroutine[Any, Any, None]: ...

    def unban(self, user_id: int, guild_id: int, *, reason: Optional[str] = ...) -> Coroutine[Any, Any, None]: ...

    def guild_voice_state(self, user_id: int, guild_id: int, *, mute: Optional[bool] = ..., deafen: Optional[bool] = ..., reason: Optional[str] = ...) -> Coroutine[Any, Any, None]: ...

    def edit_profile(self, password: str, username: str, avatar: str, **fields: Any) -> Coroutine[Any, Any, RawUserDict]: ...

    def change_my_nickname(self, guild_id: int, nickname: str, *, reason: Optional[str] = ...) -> Coroutine[Any, Any, str]: ...

    def change_nickname(self, guild_id: int, user_id: int, nickname: str, *, reason: Optional[str] = ...) -> Coroutine[Any, Any, None]: ...

    def edit_member(self, guild_id: int, user_id: int, *, reason: Optional[str] = ..., **fields: Any) -> Coroutine[Any, Any, None]: ...

    def edit_channel(self, channel_id: int, *, reason: Optional[str] = ..., **options: Any) -> Coroutine[Any, Any, RawChannelDict]: ...

    def bulk_channel_update(self, guild_id: int, data: List[_PositionDict], *, reason: Optional[str] = ...) -> Coroutine[Any, Any, None]: ...

    def create_channel(self, guild_id: int, name: str, channel_type: int, parent_id: Optional[int] = ..., permission_overwrites: Optional[List[_OverwriteDict]] = ..., *, reason: Optional[str] = ...) -> Coroutine[Any, Any, RawChannelDict]: ...

    def delete_channel(self, channel_id: int, *, reason: Optional[str] = ...) -> Coroutine[Any, Any, RawChannelDict]: ...

    def create_webhook(self, channel_id: int, *, name: str, avatar: Optional[str] = ...) -> Coroutine[Any, Any, RawWebhookDict]: ...

    def channel_webhooks(self, channel_id: int) -> Coroutine[Any, Any, List[RawWebhookDict]]: ...

    def guild_webhooks(self, guild_id: int) -> Coroutine[Any, Any, List[RawWebhookDict]]: ...

    def get_webhook(self, webhook_id: int) -> Coroutine[Any, Any, RawWebhookDict]: ...

    def get_guilds(self, limit:int, before: Optional[int] = ...,
                   after: Optional[int] = ...) -> Coroutine[Any, Any, List[RawCurrentUserGuildDict]]: ...

    def leave_guild(self, guild_id: int) -> Coroutine[Any, Any, None]: ...

    def get_guild(self, guild_id: int) -> Coroutine[Any, Any, RawGuildDict]: ...

    def delete_guild(self, guild_id: int) -> Coroutine[Any, Any, None]: ...

    def create_guild(self, name: str, region: str, icon: str) -> Coroutine[Any, Any, RawGuildDict]: ...

    def edit_guild(self, guild_id: int, *, reason: Optional[str] = ..., **fields: Any) -> Coroutine[Any, Any, RawGuildDict]: ...

    def get_bans(self, guild_id: int) -> Coroutine[Any, Any, List[RawGuildBanDict]]: ...

    def get_ban(self, user_id: int, guild_id: int) -> Coroutine[Any, Any, RawGuildBanDict]: ...

    def get_vanity_code(self, guild_id: int) -> Coroutine[Any, Any, RawInviteDict]: ...

    def change_vanity_code(self, guild_id: int, code: str, *, reason: Optional[str] = ...) -> Coroutine[Any, Any, Any]: ...

    def prune_members(self, guild_id: int, days: int, *, reason: Optional[str] = ...) -> Coroutine[Any, Any, RawGuildPruneDict]: ...

    def get_member(self, guild_id: int, member_id: int) -> Coroutine[Any, Any, RawGuildMemberDict]: ...

    def estimate_pruned_members(self, guild_id: int, days: int) -> Coroutine[Any, Any, RawGuildPruneDict]: ...

    def get_all_custom_emojis(self, guild_id: int) -> Coroutine[Any, Any, RawEmojiDict]: ...

    def get_custom_emoji(self, guild_id: int, emoji_id: int) -> Coroutine[Any, Any, RawEmojiDict]: ...

    def create_custom_emoji(self, guild_id: int, name: str, image: str, *, reason: Optional[str] = ...) -> Coroutine[Any, Any, RawEmojiDict]: ...

    def delete_custom_emoji(self, guild_id: int, emoji_id: int, *, reason: Optional[str] = ...) -> Coroutine[Any, Any, None]: ...

    def edit_custom_emoji(self, guild_id: int, emoji_id: int, *, name: str, reason: Optional[str] = ...) -> Coroutine[Any, Any, RawEmojiDict]: ...

    def get_audit_logs(self, guild_id: int, limit: int = ..., before: Optional[int] = ..., after: Optional[int] = ..., user_id: Optional[int] = ..., action_type: Optional[int] = ...) -> Coroutine[Any, Any, RawAuditLogDict]: ...

    def get_widget(self, guild_id: int) -> Coroutine[Any, Any, RawWidgetDict]: ...

    def create_invite(self, channel_id: int, *, reason: Optional[str] = ..., max_age: int = ..., max_uses: int = ..., temporary: bool = ..., unique: bool = ...) -> Coroutine[Any, Any, RawInviteDict]: ...

    def get_invite(self, invite_id: str) -> Coroutine[Any, Any, RawInviteDict]: ...

    def invites_from(self, guild_id: int) -> Coroutine[Any, Any, List[RawInviteMetaDict]]: ...

    def invites_from_channel(self, channel_id: int) -> Coroutine[Any, Any, List[RawInviteMetaDict]]: ...

    def delete_invite(self, invite_id: str, *, reason: Optional[str] = ...) -> Coroutine[Any, Any, RawInviteDict]: ...

    def edit_role(self, guild_id: int, role_id: int, *, reason: Optional[str] = ..., **fields: Any) -> Coroutine[Any, Any, RawRoleDict]: ...

    def delete_role(self, guild_id: int, role_id: int, *, reason: Optional[str] = ...) -> Coroutine[Any, Any, None]: ...

    def replace_roles(self, user_id: int, guild_id: int, role_ids: List[int], *, reason: Optional[str] = ...) -> Coroutine[Any, Any, RawGuildMemberDict]: ...

    def create_role(self, guild_id: int, *, reason: Optional[str] = ..., **fields: Any) -> Coroutine[Any, Any, RawRoleDict]: ...

    def move_role_position(self, guild_id: int, positions: List[_PositionDict], *, reason: Optional[str] = ...) -> Coroutine[Any, Any, List[RawRoleDict]]: ...

    def add_role(self, guild_id: int, user_id: int, role_id: int, *, reason: Optional[str] = ...) -> Coroutine[Any, Any, None]: ...

    def remove_role(self, guild_id: int, user_id: int, role_id: int, *, reason: Optional[str] = ...) -> Coroutine[Any, Any, None]: ...

    def edit_channel_permissions(self, channel_id: int, target: int, allow: int, deny: int, type: str, *, reason: Optional[str] = ...) -> Coroutine[Any, Any, None]: ...

    def delete_channel_permissions(self, channel_id: int, target: int, *, reason: Optional[str] = ...) -> Coroutine[Any, Any, None]: ...

    def move_member(self, user_id: int, guild_id: int, channel_id: int, *, reason: Optional[str] = ...) -> Coroutine[Any, Any, RawGuildMemberDict]: ...

    def remove_relationship(self, user_id: int) -> Coroutine[Any, Any, Any]: ...

    def add_relationship(self, user_id: int, type: Optional[int] = ...) -> Coroutine[Any, Any, Any]: ...

    def send_friend_request(self, username: str, discriminator: str) -> Coroutine[Any, Any, Any]: ...

    def application_info(self) -> Coroutine[Any, Any, RawApplicationInfoDict]: ...

    async def get_gateway(self, *, encoding: str = ..., v: int = ..., zlib: bool = ...) -> str: ...

    async def get_bot_gateway(self, *, encoding: str = ..., v: int = ..., zlib: bool = ...) -> Tuple[int, str]: ...

    def get_user_info(self, user_id: int) -> Coroutine[Any, Any, RawUserDict]: ...

    def get_user_profile(self, user_id: int) -> Coroutine[Any, Any, Any]: ...

    def get_mutual_friends(self, user_id: int) -> Coroutine[Any, Any, RawUserDict]: ...

    def change_hypesquad_house(self, house_id: int) -> Coroutine[Any, Any, Any]: ...

    def leave_hypesquad_house(self, house_id: int) -> Coroutine[Any, Any, None]: ...

    def edit_settings(self, *, afk_timeout: int = ..., animate_emojis: bool = ..., convert_emoticons: bool = ...,
                      default_guilds_restricted: bool = ..., detect_platform_accounts: bool = ...,
                      developer_mode: bool = ..., disable_games_tab: bool = ..., enable_tts_command: bool = ...,
                      explicit_content_filter: int = ..., friend_source_flags: int = ...,
                      gif_auto_play: bool = ..., guild_positions: List[int] = ...,
                      inline_attachment_media: bool = ..., inline_embed_media: bool = ..., locale: str = ...,
                      message_display_compact: bool = ..., render_embeds: bool = ..., render_reactions: bool = ...,
                      restricted_guilds: List[int] = ..., show_current_game: bool = ...,
                      status: str = ..., theme: str = ...,
                      timezone_offset: int = ...) -> Coroutine[Any, Any, RawClientUserDict]: ...
