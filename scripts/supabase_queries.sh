weather_api() {
 ENDPOINT=$1
 shift
 https "$SUPABASE_API_URL/$ENDPOINT" "$@" "$SUPABASE_API_HEADERS"
}
alias wapi=weather_api

# https get https://ddmuzakoxacxxjlbewdc.supabase.co/rest/v1/samples?select=* "apikey:$SUPABASE_KEY" "Authorization: Bearer $SUPABASE_KEY"
# wapi "samples?select=*"