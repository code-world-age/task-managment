create CREATE TABLE IF NOT EXISTS api.api_user
(
    user_id integer NOT NULL DEFAULT nextval('api.api_user_user_id_seq'::regclass),
    user_name character varying(100) COLLATE pg_catalog."default" NOT NULL,
    created_at timestamp with time zone NOT NULL DEFAULT CURRENT_TIMESTAMP,
    modified_at timestamp with time zone,
    CONSTRAINT api_user_pkey PRIMARY KEY (user_id)
)